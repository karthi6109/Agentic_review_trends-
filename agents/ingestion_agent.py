
from google_play_scraper import reviews
from collections import defaultdict
import json

def fetch_reviews(app_id, count=500):
    result, _ = reviews(
        app_id,
        lang="en",
        country="in",
        count=count
    )

    daily = defaultdict(list)
    for r in result:
        date = r['at'].strftime('%Y-%m-%d')
        daily[date].append(r['content'])

    with open("data/raw_reviews.json", "w") as f:
        json.dump(daily, f, indent=2)

    return daily
