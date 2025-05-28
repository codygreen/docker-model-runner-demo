from hn_api import get_best_story_ids, get_story_item
from scraper import scrape_url
from summarizer import summarize_with_gemma3
NUM_STORIES = 5

def main():
    story_ids = get_best_story_ids(NUM_STORIES)  # Pass limit to API

    for story_id in story_ids:
        story = get_story_item(story_id)
        url = story.get("url")
        title = story.get("title")

        if not url:
            print(f"Skipping story {story_id} (no URL)")
            continue

        print(f"\nProcessing: {title} ({url})")
        article_text = scrape_url(url)
        summary = summarize_with_gemma3(article_text)
        print(f"\nSummary:\n{summary}\n{'-'*80}")

if __name__ == "__main__":
    main()
