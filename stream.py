import tweepy as tpy
from bot import Bot

class Stream(tpy.StreamListener):
    def __init__(self, bot):
        self.bot = bot
        self.api = bot.api

    def on_status(self, keywords):
        tweets = self.api.mentions_timeline()
        for tweet in tweets:
            if tweet.in_reply_to_status_id is not None:
                continue

            # if any(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet.favorited:
                self.api.create_favorite(tweet.id)

            if not tweet.user.following:
                tweet.user.follow

            self.api.update_status(
                status=f"@{tweet.user.screen_name} It's good to see you liked my tweets. Check me out!",
                in_reply_to_status_id=tweet.id
            )

consumer_key = ""
consumer_secret = ""
access_token = ""
acces_token_secret = ""

bot_test = Bot(consumer_key, consumer_secret,
               access_token, acces_token_secret)

stream = Stream(bot_test)
# keywords = ['Python', 'Java']
# stream.on_status(keywords)



