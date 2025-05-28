import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def get_best_story_ids(limit=None):
    response = requests.get(f"{BASE_URL}/beststories.json")
    response.raise_for_status()
    story_ids = response.json()
    if limit is not None:
        return story_ids[:limit]
    return story_ids

def get_story_item(story_id):
    response = requests.get(f"{BASE_URL}/item/{story_id}.json")
    response.raise_for_status()
    return response.json()
