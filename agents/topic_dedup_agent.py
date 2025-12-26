import json
import os
import difflib


def load_topics():
    try:
        with open("taxonomy/canonical_topics.json") as f:
            return json.load(f)
    except Exception:
        return {}


def save_topics(data):
    with open("taxonomy/canonical_topics.json", "w") as f:
        json.dump(data, f, indent=2)


def _local_normalize(topic, canon):
    # simple similarity-based normalization using difflib
    for c in canon:
        ratio = difflib.SequenceMatcher(None, topic.lower(), c.lower()).ratio()
        if ratio > 0.78 or topic.lower() in c.lower() or c.lower() in topic.lower():
            return c
    canon[topic] = {}
    return topic


def normalize(topic, canon):
    # try OpenAI if available, otherwise local normalize
    try:
        import openai
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            openai.api_key = api_key
            for c in canon:
                prompt = f"Are '{topic}' and '{c}' the same topic? Answer YES or NO."
                r = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    timeout=10
                )
                if "YES" in r.choices[0].message.content.upper():
                    return c
    except Exception:
        pass

    return _local_normalize(topic, canon)
