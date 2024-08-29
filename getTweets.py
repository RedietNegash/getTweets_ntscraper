import pytz
from datetime import datetime, timedelta
from ntscraper import Nitter

scraper = Nitter(log_level=0, skip_instance_check=False)
scraper.instance = "https://nitter.woodland.cafe/"

def fetch_24_hour_tweets():
    tweets = scraper.get_tweets('BarackObama', mode="user", number=50)
    if tweets['tweets']:
        data = {
            'text': [],
            'date': [],
        }

        timezone = pytz.timezone("America/New_York")
        current_time = datetime.now(timezone)
        last_24_hours = current_time - timedelta(hours=24)

        for tweet in tweets['tweets']:
            try:
                tweet_time = datetime.strptime(tweet['date'], '%b %d, %Y · %I:%M %p %Z')
                tweet_time = tweet_time.astimezone(timezone)

                if tweet_time >= last_24_hours:
                    data['text'].append(tweet['text'])
                    data['date'].append(tweet_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
            except ValueError as e:
                print(f"Date parsing error: {e}")

        if data['text']:
            for i in range(len(data['text'])):
                print(f"Date: {data['date'][i]}")
                print(f"Tweet: {data['text'][i]}")
                print("-" * 40)
        else:
            print("No tweets from the last 24 hours.")
    else:
        print("No tweets were fetched. The instance may be rate-limited.")

fetch_24_hour_tweets()
