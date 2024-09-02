from datetime import timedelta

broker_url = 'redis://localhost:6379/1'
backend_url='redis://localhost:6379/1'



beat_schedule = {
    'fetch-tweets-every-minute': {
        'task': 'getTweets.fetch_24_hour_tweets',
        'schedule': timedelta(hours=24),
        'args': (['BarackObama', 'elonmusk'],),
    },
}

timezone = 'UTC'
