
import pandas as pd
from agents.ingestion_agent import fetch_reviews
from agents.topic_extraction_agent import extract_topics
from agents.topic_dedup_agent import load_topics, save_topics, normalize
from agents.trend_aggregation_agent import aggregate

APP_ID = "in.swiggy.android"

reviews = fetch_reviews(APP_ID)
canon = load_topics()
daily_topics = {}

for date, revs in reviews.items():
    daily_topics[date] = []
    for r in revs:
        for t in extract_topics(r):
            daily_topics[date].append(normalize(t, canon))

save_topics(canon)

trend = aggregate(daily_topics)
df = pd.DataFrame(trend).fillna(0).astype(int).T.sort_index(axis=1)
df.to_csv("output/trend_report.csv")
print("Trend report generated")
