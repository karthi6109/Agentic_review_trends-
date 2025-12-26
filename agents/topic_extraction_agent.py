
import openai
import os
import re
from pathlib import Path

SYSTEM_PROMPT = "Extract issues, complaints or feature requests as short topics."

# lightweight stopwords
STOPWORDS = {
    "the", "and", "for", "this", "that", "with", "from", "have", "has",
    "was", "were", "are", "but", "not", "you", "your", "it's", "its",
    "i", "me", "my", "we", "our", "they", "them", "on", "in", "to",
    "is", "be", "of", "a", "an", "it"
}

KEYWORDS = [
    "crash", "login", "payment", "delivery", "refund", "order", "slow",
    "lag", "bug", "feature", "update", "install", "network", "wifi",
    "ads", "battery", "notification", "search", "signup", "subscription",
    "tracking", "timeout", "error"
]


def _local_extract(review, top_k=3):
    r = review.lower()
    topics = []

    for kw in KEYWORDS:
        if kw in r and kw not in topics:
            topics.append(kw)

    if not topics:
        tokens = re.findall(r"[a-zA-Z0-9]{4,}", r)
        freq = {}
        for t in tokens:
            if t in STOPWORDS:
                continue
            freq[t] = freq.get(t, 0) + 1
        sorted_tokens = sorted(freq.items(), key=lambda x: -x[1])
        for t, _ in sorted_tokens[:top_k]:
            if t not in topics:
                topics.append(t)

    return topics


def extract_topics(review):
    # prefer env var OPENAI_API_KEY; fallback to data/openai_key.txt
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        key_path = Path(__file__).resolve().parents[1] / "data" / "openai_key.txt"
        if key_path.exists():
            api_key = key_path.read_text().strip()

    if api_key:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": review}
                ],
                timeout=15
            )
            text = response.choices[0].message.content
            return [t.strip().lower() for t in text.split(",") if t.strip()]
        except Exception:
            return _local_extract(review)
    else:
        return _local_extract(review)
