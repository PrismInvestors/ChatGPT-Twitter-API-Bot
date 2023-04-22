import tweepy
import openai
import datetime
from datetime import datetime, timezone
import time
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
twitter_name = config.twitter_name
filter_tweets = config.filter_tweets
requirement = config.requirement
prompt = config.prompt
# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ChatGPT API key
openai.api_key = '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'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']['content']


try:
    print("Starting a new loop iteration...")  # Add this line
    highest_retweet_count = 0
    target_tweet = None
    target_username = None
    def save_tweets(tweets, filename):
        with open(filename, "w") as file:
            for tweet_id in tweets:
                file.write(str(tweet_id) + "\n")

    def load_tweets(filename):
        tweets = set()
        try:
            with open(filename, "r") as file:
                for line in file:
                    tweets.add(int(line.strip()))
        except FileNotFoundError:
            pass
        return tweets

    replied_tweets = load_tweets("replied_tweets.txt")

    highest_retweet_count = 0
    target_tweet = None
    target_username = None


    # Get the latest 200 tweets from the home timeline
    tweets = api.home_timeline(count=200)

    # Get the list of screen names of users that you are following
    following = [user.screen_name for user in api.get_friends()]

    # Filter out the tweets that are not from the users you are following
    filtered_tweets = []
    for tweet in tweets:
        if tweet.user.screen_name in following:
            filtered_tweets.append(tweet)

    for tweet in tweets:
        username = tweet.user.screen_name
        tweet_age = (datetime.now(timezone.utc) - tweet.created_at).total_seconds()
        # Check if the tweet was posted within the last hour (3600 seconds) and the tweet author is not your account
        if tweet_age <= 6400 and tweet.retweet_count > highest_retweet_count and tweet.id not in replied_tweets and tweet.text.strip() != "" and username != {twitter_name}:
            highest_retweet_count = tweet.retweet_count
            target_tweet = tweet
            target_username = username

    def get_valid_response(prompt):
        while True:
            response = generate_response(prompt)
            if "t.co" not in response:  # Change this line to check if "t.co" is present anywhere in the response
                return response
    def meets_requirement(tweet_text):
        if not filter_tweets:
            return True
        prompt = f"OUTPUT: Reply only YES or NO\nPROMPT: {requirement}?\n\nTweet: {tweet_text}"
        response = generate_response(prompt).strip().lower()
        while "yes" not in response and "no" not in response:
            response = generate_response(prompt).strip().lower()
        return "yes" in response
    if target_tweet:
        # Add the tweet ID to the replied list and save to file
        replied_tweets.add(target_tweet.id)
        save_tweets(replied_tweets, "replied_tweets.txt")
        if meets_requirement(target_tweet.text):
            prompt2 = f"Based on the tweet below, {prompt} Output should include nothing but the tweet. Do not include any other text or characters, only output the intended tweet: \n\nTWEET:\n{target_tweet.text}"
            response = get_valid_response(prompt2)
            if ':' in response:
                response = response.split(':', 1)[1].lstrip()
            try:
                # Like the original tweet
                api.create_favorite(target_tweet.id)
                print("Posting quote tweet...")  # Add this line
                original_tweet_url = f"https://twitter.com/{target_username}/status/{target_tweet.id}"
                quote_tweet_text = f"{response} {original_tweet_url}"
                quote_tweet = api.update_status(status=quote_tweet_text, attachment_url=original_tweet_url)
            except tweepy.Forbidden as e:
                print("Cannot heart and quote tweet the same tweet twice. Blacklisting the tweet.")
        else:
            print("Tweet is either not related to crypto/finance or is an airdrop/giveaway. Skipping.")
    else:
        print("No tweets found within the last 12 hours")

except ConnectionError as e:
    print(f"Connection error: {e}. Reconnecting...")
    time.sleep(2)  # Wait 10 seconds before retrying

except Exception as e:
    print(f"Unexpected error: {e}")
