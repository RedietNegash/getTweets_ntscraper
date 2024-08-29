import pytz
from datetime import datetime, timedelta
from ntscraper import Nitter

scraper = Nitter(log_level=0, skip_instance_check=False)
scraper.instance = "https://nitter.woodland.cafe/"

def fetch_24_hour_tweets(users):
    timezone = pytz.timezone("America/New_York")  
    current_time = datetime.now(timezone)
    last_24_hours = current_time - timedelta(hours=24)

    for user in users:
        print(f"Fetching tweets for user: {user}")
        tweets = scraper.get_tweets(user, mode="user")
        
        if tweets['tweets']:
            data = {
                'text': [],
                'date': [],
            }

            for tweet in tweets['tweets']:
                tweet_time = datetime.strptime(tweet['date'], '%b %d, %Y · %I:%M %p %Z').replace(tzinfo=pytz.utc).astimezone(timezone)
                if tweet_time >= last_24_hours:
                    data['text'].append(tweet['text'])
                    data['date'].append(tweet_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

            if data['text']:
                for i in range(len(data['text'])):
                    print(f"Date: {data['date'][i]}")
                    print(f"Tweet: {data['text'][i]}")
                    print("-" * 40)
            else:
                print(f"No tweets from the last 24 hours for user: {user}.")
        else:
            print(f"No tweets were found for user: {user}.")


users = ['BarackObama', 'elonmusk']
fetch_24_hour_tweets(users)
