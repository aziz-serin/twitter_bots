import tweepy

class bot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def check_validity(self):
        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

    def latest_tweet_keyword(self, keyword, amount):
        try:
            for tweet in self.api.search(q=keyword, lang="en", rpp=amount):
                self.api.update_status(f"{tweet.user.name}:{tweet.text}")
        except:
            print("Make sure your keyword is in a String format and amount is in integer format.",
                  " If they are both correct, make sure the keys you provided are valid with check_validity method")

    def update_status(self, status):
        self.api.update_profile(description=status)

bot_test = bot("consumer_key", "consumer_secret",
               "access_token", "access_token_secret")
#bot_test.check_validity()
#bot_test.latest_tweet_keyword("Java", "4")
#bot_test.update_status("Hi, I am a friendly bot. You wanna check what I did here?")