import json

def load_keywords():
    with open('keywords.json') as f:
        return json.load(f)

def suggest_hashtags(description):
    keywords = load_keywords()
    desc_lower = description.lower()
    hashtags = set()

    for topic, tags in keywords.items():
        if topic in desc_lower:
            hashtags.update(tags)
    return list(hashtags) if hashtags else ["#instagood", "#photooftheday", "#love"]