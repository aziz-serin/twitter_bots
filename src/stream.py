# Python script to filter through other people's tweets,
# then reply to them or send a direct message.

# Import necessary packages

import tweepy as tpy
from tweepy import TweepError
from src.bot import Bot

# Twitter Stream object, inherits from StreamListener, and it is necessary to inherit
# to override the methods

class Stream(tpy.StreamListener):

    def __init__(self, bot):
        self.bot = bot
        self.api = bot.api

    # Gets the tweets which your account is mentioned in,
    # likes it and followes it's author, and replies to it

    def on_status(self):
        tweets = self.api.mentions_timeline()
        for tweet in tweets:
            if tweet.in_reply_to_status_id is not None:
                continue

            if not tweet.favorited:
                self.api.create_favorite(tweet.id)

            if not tweet.user.following:
                tweet.user.follow

            self.api.update_status(
                status=f"@{tweet.user.screen_name} It's good to see you liked my tweets. Check me out!",
                in_reply_to_status_id=tweet.id
            )

    # Gets the tweets which your account is mentioned in,
    # likes it and followes it's author, and sends a direct message to
    # the author if the author can recieve a message

    def message_mentions(self):
        tweets = self.api.mentions_timeline()
        for tweet in tweets:
            try:
                if tweet.in_reply_to_status_id is not None:
                    continue

                if not tweet.favorited:
                    self.api.create_favorite(tweet.id)

                if not tweet.user.following:
                    tweet.user.follow

                self.api.send_direct_message(tweet.user.id,
                                             "Looks like you enjoyed what I did there, wanna check me out?")
            except TweepError:
                print('You cannot message to this user by Twitter rules.')


consumer_key = ""
consumer_secret = ""
access_token = ""
acces_token_secret = ""

bot_test = Bot(consumer_key, consumer_secret,
               access_token, acces_token_secret)

# bot_test.check_validity()
stream = Stream(bot_test)
# stream.message_mentions()

# keywords = ['Python', 'Java']
# stream.on_status(keywords)



