# Docker Model Runner Demo

This repository demonstrates how to use [Docker Model Runner](https://www.docker.com/blog/introducing-docker-model-runner/) in both development and production environments. It provides a practical example: summarizing top news stories from Hacker News using a large language model (LLM) running in Docker.

---

## Overview

This demo application:

- Fetches the best stories from Hacker News.
- Retrieves and stores story metadata and content in a PostgreSQL database.
- Uses a quantized Gemma 3 LLM (via Docker Model Runner) to generate concise summaries of each article.
- Avoids redundant work by checking if a story and its summary already exist in the database.

---

## How It Works

**Workflow:**

1. **Fetch Best Stories:**  
    Retrieve the list of top story IDs from the Hacker News API.

2. **Get Story Metadata:**  
    For each ID, fetch detailed metadata (title, URL, etc.).

3. **Check Database:**  
    If the story and its summary already exist in PostgreSQL, skip processing.

4. **Scrape Article Content:**  
    Download the article HTML using the story's URL.

5. **Summarize with LLM:**  
    Send the article content to the Gemma 3 model via Docker Model Runner to generate a summary.

6. **Store Results:**  
    Save the story metadata, content, and summary in the database.

**Notes:**

- Uses the Firebase client library as recommended by the [Hacker News API](https://github.com/HackerNews/API).
- Handles errors for unreachable or non-HTML URLs.
- All data is persisted in PostgreSQL (managed by Docker Compose).

---

## Development Environment

This project uses a VS Code dev container (see [`.devcontainer`](./.devcontainer)) for a consistent Python development setup with Docker and PostgreSQL. The dev container:

- Installs Python, Docker CLI, Git, and GitHub CLI.
- Uses Docker Compose to run both the app and PostgreSQL as services (see `.devcontainer/docker-compose.yml`).
- Lets you develop, test, and run everything inside the container—no need to install dependencies on your host.

---

## Getting Started

### 1. Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Docker Model Runner enabled.
- VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

### 2. Verify Docker Model Runner

Check that Docker Model Runner is running:

```bash
docker model status
```

You should see output similar to:

```
Docker Model Runner is running

Status:
llama.cpp: running llama.cpp latest-metal (sha256:...)
```

### 3. Pull the Gemma 3 Model

Download the quantized Gemma 3 model from Docker Hub:

```bash
docker model pull ai/gemma3:4B-Q4_K_M
```

### 4. Build and Run the Demo

Clone the repository and start the containers:

```bash
cd hackernews-summary
docker compose up --build --exit-code-from app
```

- The app will process stories and exit when done.
- The PostgreSQL container will stop automatically.

---

## Additional Tips

- All required tools (`docker`, `git`, `gh`, `python3`, etc.) are pre-installed in the dev container.

---

## References

- [Docker Model Runner Documentation](https://docs.docker.com/model-runner/)
- [Hacker News API](https://github.com/HackerNews/API)
- [Gemma 3 Model on Docker Hub](https://hub.docker.com/layers/ai/gemma3/4B-Q4_K_M/images/sha256-0b329b335467cccf7aa219e8f5e1bd65e59b6dfa81cfa42fba2f8881268fbf82)

---

**Summary:**  
This project provides a hands-on example of using Docker Model Runner to run LLMs in a reproducible, containerized environment. Follow the steps above to fetch, summarize, and store Hacker News stories using state-of-the-art tooling.