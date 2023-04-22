# Twitter API keys and secrets

consumer_key = "Consumer Key"
consumer_secret = "Consumer Secret"
access_token = "Access Token"
access_token_secret = "Access Token Secret"
twitter_name = "TwitterHandle  (no @)"

# ChatGPT API key
openai_api_key = 'openAIkey'

#ChatGPT Prompt (change to whatever you like! The code will append it with some extra prompting to ensure the tweet is successful in main.py)
prompt = "Write a very short tweet reply that mirrors the mood of the original tweet."

#If True, will use the Tweet requirement below to attempt to filter some tweets based on the content of the tweet to be replied to.
filter_tweets = True #or False

#Tweet Requirement (change this to any requirement that you could like to use to filter responses. Use a yes or no question)
requirement = "EXAMPLE: Is the following tweet a crypto airdrop/giveaway tweet?"

#Based on the example requirement, if the tweet IS a crypto airdrop/giveaway tweet, the chatGPT will return YES and the tweet will not be quote tweeted.