from hn_api import get_best_story_ids, get_story_item
from scraper import scrape_url
from summarizer import summarize_with_gemma3
from db import Story, SessionLocal, init_db
NUM_STORIES = 5

def main():
    init_db()
    session = SessionLocal()
    story_ids = get_best_story_ids(NUM_STORIES)  # Pass limit to API

    for story_id in story_ids:
        # Check if story with summary already exists
        db_story = session.query(Story).filter_by(hn_id=story_id).first()
        if db_story and db_story.summary:
            print(f"Skipping story {story_id} (already summarized in DB)")
            continue

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

        if not db_story:
            db_story = Story(hn_id=story_id, title=title, url=url, content=article_text, summary=summary)
            session.add(db_story)
        else:
            db_story.title = title
            db_story.url = url
            db_story.content = article_text
            db_story.summary = summary
        session.commit()
    session.close()

if __name__ == "__main__":
    main()
