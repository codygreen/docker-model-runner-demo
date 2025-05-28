# Docker Model Runner Demo

The purpose of this repository is to demonstrate the use of Docker Model Runner both in a development and testing environment

## Install

Follow the [Docker Model Runner](https://docs.docker.com/model-runner/) documentation to ensure your running on a compatible device and have the required version of Docker Desktop.

## Test App

This test application will fetch and summarize top news stories from Hacker News using their public API.

Workflow:

1. Fetch Best Stories:
    - Retrieve the list of current best story IDs from the Hacker News API endpoint: https://hacker-news.firebaseio.com/v0/beststories.json

1. Retrieve Story Metadata:
    - For each story ID, fetch detailed metadata using the item endpoint: https://hacker-news.firebaseio.com/v0/item/<story_id>.json

1. Scrape Story Content:
    - Extract the url field from each story object.
    - Perform an HTTP GET request to retrieve the raw HTML content of the external article.

1. Generate Summary with LLM:
    - Provide the scraped article content to the Gemma 3 language model.
    - Request a concise summary of the article from the model.

Notes:

- The application uses the Firebase client library as described in the Hacker News API GitHub repository.
- Error handling for unreachable URLs or non-HTML responses should be included.