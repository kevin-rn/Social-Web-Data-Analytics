from __future__ import absolute_import, print_function
from datetime import datetime
import time
import tweepy
import json

# The consumer key and secret
# consumer_key = 'CONSUMER_KEY'
# consumer_secret = 'CONSUMER_SECRET'

# Access token
# access_token = 'ACCESS_TOKEN'
# access_token_secret = 'ACCESS_TOKEN_SECRET'

# Bearer Token
bearer_token = 'BEARER_TOKEN'


class StdOutListener(tweepy.StreamingClient):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, timer_limit):
        super().__init__(bearer_token=bearer_token)

        # Keep track of time passed and total number of tweets crawled.
        self.timer_start = time.time()
        self.timer_limit = timer_limit
        self.starting_time = datetime.now()
        self.file_contents = list()
        self.counter = 0

    def on_data(self, data):
        if (time.time() - self.timer_start) > self.timer_limit:
            print(f"Start time: {self.starting_time} - End time: {datetime.now()} - Count: {self.counter}")
            # Task 1.2
            # with open('fetched_tweets.json', 'w', encoding="utf-8") as output_file:
            #     json.dump(self.file_contents, output_file, ensure_ascii=False, indent=4)

            # Force it to stop running due to issue with program continuing to run despite 'return False'.
            self.running = False

            return False
        else:
            # Task 1.2
            # self.file_contents.append(json.loads(data))

            self.counter += 1
            print(data)
            return True

    def on_error(self, status):
        print(f"Error encountered with status: {status}")
        return False


if __name__ == '__main__':
    # Task 1.2 - 10 min
    time_duration = 600

    # Task 1.3 - 2 hours
    # time_duration = 7200

    listener = StdOutListener(timer_limit=time_duration)

    try:
        # Task 1.2
        listener.sample()

        # Task 1.3 - Crawl tweets sent from Amsterdam geo coordinates.
        # rule = tweepy.StreamRule("bounding_box:[4.61 52.27 5.07 52.5]")

        # Task 1.3 - Crawl tweets related to COVID-19 using related terms.
        # rule = tweepy.StreamRule("covid OR covid-19 OR corona OR coronavirus OR lockdown")

        listener.add_rules(rule)
        listener.filter()
    except KeyboardInterrupt:
        print('Ended on Keyboard interrupt')
