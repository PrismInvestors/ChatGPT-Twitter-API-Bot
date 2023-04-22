# Python Twitter Script

This project contains a Python script to interact with the Twitter API.

## Installation

Before running the script, make sure to install the required packages. You can do this by running the following command:

```bash
pip install -r requirements.txt


Usage
After installing the required packages, and completing the setup requirements below, you can run the .bat file "run.bat"

##Setup

Be sure to add your API keys for Twitter and OpenAI in the config.py

##For Twitter API

1. Go to:
https://developer.twitter.com/en/portal/dashboard

2a. Click on the default app and click "EDIT"
2b. Delete the default app

3a. Click on the default project and click "EDIT"
3b. Delete the default app

4. Start a new standalone app
5. Complete the setup and go to "Keys and Tokens"
6. Get the Consumer Keys -> API Key and Secret and put them in config.py
7. Get the Authentication Tokens -> Access Token and Secret and put them in config.py
8. Go to settings under "User authentication settings" and click "Edit"
9. Set the App permissions to "Read and write"
10. Set the type of App to "Web App, Automated App or Bot"
11. Set the Callback URI to http://127.0.0.1:8000
12. Set the Website URL to any URL 
13. Click Save

14. Enter your Twitter handle in the config.py without the preceding @ symbol

Your Twitter setup is complete!

#For OpenAI API

To get your OpenAI API key, go to:

https://platform.openai.com/account/api-keys

Put the API key into your config.py