import tweepy

# A google and twitter account as been created for the bot
# deleted :(

# Twitter API keys
# deleted :(


# Authenticate to Twitter
def api():
    auth = tweepy.OAuthHandler(APIKEY, APIKEYSECRET)
    auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)
    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    print("Tweeted: " + message)


if __name__ == "__main__":
    api = api()
    tweet(api, "Hello world!")
