from __future__ import absolute_import, print_function
from datetime import datetime
import time
import tweepy

# The consumer key and secret
consumer_key = "bSo8MvmycDYZgEvcCYrphSGdY"
consumer_secret = "A7DwGZyRxI4QjLXSqIP1MuFO3VUbX07kXdcX3Rh7aBr2chu6yX"

# Access token
access_token = "1586041576639406082-WFU5jeCy6URmA52dQuEl703f2HgN4R"
access_token_secret = "RsXbzSXEi64rCIrX1oVVnz4CGXHOQvFrQP8HVGV5xeh4P"

# Filters for Task 1.3
AMSTERDAM_GEO = [4.61, 52.27, 5.07, 52.5]
COVID_KEYWORDS = ["covid", "covid-19", "corona", "coronavirus", "lockdown"]


class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, timer_limit):
        super().__init__()

        # Keep track of time passed and total number of tweets crawled.
        self.timer_start = time.time()
        self.timer_limit = timer_limit
        self.starting_time = datetime.now()
        self.counter = 0

    def on_data(self, data):

        timer = time.time() - self.timer_start
        if timer < self.timer_limit:
            self.counter += 1

            # Append data to file
            with open('fetched_tweets.txt', 'a') as tf:
                tf.write(data)

            print(data)
            return True
        else:
            print(f"Start time: {self.starting_time} \n End time: {datetime.now()} \n Count: {self.counter}")
            return False

    def on_error(self, status):
        print(f"Error encountered with status: {status}")


if __name__ == '__main__':
    # measure 10 min
    listener = StdOutListener(timer_limit=600)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:
        stream = tweepy.Stream(auth, listener)
        stream.sample()

        # # Crawl tweets sent from Amsterdam
        # stream.filter(locations=AMSTERDAM_GEO)
        #
        # # Crawl tweets related to COVID-19
        # stream.filter(track=COVID_KEYWORDS)
    except KeyboardInterrupt:
        print('Ended on Keyboard interrupt')
