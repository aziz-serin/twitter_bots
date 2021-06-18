# Python script to use twitter API and perform various actions

#import modules
import tweepy as tpy
import time as t
from tweepy import TweepError

# Initialise the class with four parameters which are the keys provided by twitter.

class Bot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tpy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tpy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # Check if your keys are all valid

    def check_validity(self):
        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except TweepError:
            print("Error during authentication")

    # Retweet latest tweets with the specified keyword, also in specified amount, and like them

    def latest_tweet_keyword(self, keyword, amount):
        try:
            for tweet in tpy.Cursor(self.api.search, q= keyword,tweet_mode='extended', include_rts=False).items(amount):
                status = self.api.get_status(tweet.id)
                retweeted = status.retweeted
                tweettext = str(tweet.full_text.lower().encode('ascii', errors='ignore'))


                if (retweeted == False) and (tweettext.startswith("rt @") == False):
                    self.api.update_status(tweet.full_text)
                    self.api.create_favorite(tweet.id)
        except TweepError:
            print("Make sure your keyword is in a String format and amount is in integer format.",
                  " If they are both correct, make sure the keys you provided are valid with check_validity method")

    # Update profile description

    def update_status(self, status):
        self.api.update_profile(description=status)

    # Upload a profile image with the file path

    def update_image(self, file_name):
        try:
            self.api.update_profile_image(filename = file_name)
        except TweepError:
            print("Your file format should be either GIF, JPEG, or PNG."
                  "Check your file format or make sure your file path is valid. ")

    # Update profile name and location

    def update_profile(self, name, location):
        self.api.update_profile(name = name, location = location)

    # Check latest trends

    def check_trends(self):
        trends_result = self.api.trends_available()
        for trend in trends_result[0]["trends"]:
            print(trend["name"])

    # Follow every person who is following you

    def follow_followers(self):
        for follower in tpy.Cursor(self.api.followers).items():
            if not follower.following:
                follower.follow()
                t.sleep(1)

    # Follow a person with their username (The unique one, which you cannot change)

    def follow_users(self, user_name):
        try:
            self.api.create_friendship(user_name)
        except TweepError:
            print('Make sure the username you entered is valid.')

    # Print latest tweets a user posted, including yourselves.

    def print_timeline(self, user_name, amount):
        try:
            if user_name == "home":
                timeline = self.api.home_timeline(count = amount)
                for tweet in timeline:
                    print(f"{tweet.user.name} said {tweet.text}")
            else:
                timeline = self.api.user_timeline(screen_name = user_name, count=amount)
                for tweet in timeline:
                    print(f"{tweet.user.name} said {tweet.text}")
        except TweepError:
            print("Check the username you provided.")

    # Create a tweet and post it.

    def tweet_manually(self, tweet):
        self.api.update_status(tweet)

    # List your message activity, the ones you sent and received

    def list_message_activity(self):
        messages = self.api.list_direct_messages()
        for message in messages:
            print(f"{self.api.get_user(message.message_create['sender_id']).screen_name}"
                  f" said {message.message_create['message_data']['text']}")

    # Sent messages to a user using their username

    def send_messages(self, user_name, message):
        try:
            user = self.api.get_user(user_name)
            user_id = user.id
            self.api.send_direct_message(user_id, message)
        except TweepError:
            print("Check the username you have entered.")

    # Block a specified user

    def block_users(self, screen_name):
        self.api.create_block(screen_name=screen_name)

    # Unblock the users you blocked before

    def unblock_users(self, screen_name):
        try:
            self.api.destroy_block(screen_name=screen_name)
        except TweepError:
            print("Maybe you unblocked this user, "
                  "or the username you entered is invalid. Try again")

    # Get the list of the users who you blocked

    def see_blocked_users(self):
        blocked_list = self.api.blocks()
        for user in blocked_list:
            print(f"Blocked: {user.name} known as {user.screen_name}")

    # Report spamming users using their username

    def report_spam(self, screen_name):
        try:
            self.api.report_spam(screen_name=screen_name)
        except TweepError:
            print('Username may not exist, try again.')

    # Return information about your profile in a json format

    def return_me(self):
        return self.api.me()

    # Return information about another user in a json format

    def return_users(self, username):
        try:
            return self.api.get_user(screen_name=username)
        except TweepError:
            print('Username may not exist, try again')

    # Works the same way as twitter search function. Returns information in json format

    def search_users(self, keyword, number_of_statuses):
        return self.api.search_users(q=keyword, count=number_of_statuses)

    # Fetches the tweets which you are mentioned in, likes them and follows its author

    def follow_like_mentioned(self):
        tweets = self.api.mentions_timeline()
        for tweet in tweets:
            if tweet.favorited == False:
                self.api.create_favorite(tweet.id)
            if tweet.user.following == False and tweet.user.follow_request_send == False:
                tweet.user.follow()

consumer_key = ""
consumer_secret = ""
access_token = ""
acces_token_secret = ""

bot_test = Bot(consumer_key, consumer_secret,
               access_token, acces_token_secret)

# To print links on terminal, or generate one to post in other places, the following code may help you!

#Example:

# import urllib.parse
# s = urllib.parse.quote("github.com/aziz-serin/twitter_bots")
# link = "https://"+s

