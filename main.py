# Simple terminal gui with an example bot

# Necessary imports

from src.bot import Bot
from src.stream import Stream
from time import sleep
import random
from tweepy import TweepError

# A function with the relevant information and a simple bot.

def main():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    acces_token_secret = ""
    bot_test = Bot(consumer_key, consumer_secret,
                   access_token, acces_token_secret)
    stream = Stream(bot_test)

    # Check terminal inputs

    while True:
        try:
            a = int(input("Welcome to Twitter Bot. Enter 1 to see more information on a general bot"
                "or 2 to run a stream filter: "))
            if a == 1 or a == 2:
                break
            else:
                print("Invalid number, try again:")
                continue
        except ValueError:
            print("Make sure you entered an integer!")

    if a == 1:
        methods_list = help(Bot) #Lists the methods of Bot class in the terminal
        print("\n" + 'Have a look at the provided modules, and play around with them as you like!')

    # Select a random topic from the list, retweet the latest 5 tweets about that topic,
    # reply if anyone mentions you, and then send a dm if you can to users who mentioned you

    elif a == 2:
        keywords = ['Python', 'Java', 'C', 'Programming', 'Coding', 'Machine Learning',
                    'AI', 'Swift', 'Rust', 'C#', 'Javascript', 'Node.js', 'Kotlin', 'Web Development',
                    'Ruby', 'Haskell', 'React.js', 'Django', 'API', 'HTML', 'CSS']
        while True:
            try:
                rand_int = random.randint(0, len(keywords))
                keyword = keywords[rand_int]
                bot_test.latest_tweet_keyword(keyword, 5)
                sleep(600)
                stream.on_status()
                sleep(600)
                stream.message_mentions()
                sleep(3600)
            except TweepError:
                print('An error has occured.')

if __name__ == "__main__":
    main()
