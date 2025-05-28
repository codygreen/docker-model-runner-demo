# Docker Model Runner Demo

This guide introduces the benefits of [Docker Model Runner](https://www.docker.com/blog/introducing-docker-model-runner/) and demonstrates its use in both development and production environments. The included example shows how to summarize top Hacker News stories using a large language model (LLM) running in Docker.

## Why Docker Model Runner?

Docker Model Runner offers several advantages for AI-powered application development:

- **Local, Secure Development:** Run models locally in a secure, compliant environment.
- **OpenAI-Compatible Endpoints:** Easily switch between local and cloud AI services without code changes.
- **Enterprise Integration:** Works with Docker Desktop, reducing the need for additional software approvals.
- **Hardware Acceleration:** Leverage Mac Silicon or NVIDIA GPU acceleration without complex setup.

## What’s in This Demo?

This repository provides a practical example that:

- Fetches top stories from Hacker News.
- Stores story metadata and content in PostgreSQL.
- Uses a quantized Gemma 3 LLM (via Docker Model Runner) to generate concise summaries.
- Avoids redundant work by checking if a story and its summary already exist in the database.

## How It Works

**Workflow:**

1. **Fetch Best Stories:** Retrieve top story IDs from the Hacker News API.
2. **Get Story Metadata:** Fetch details (title, URL, etc.) for each story.
3. **Check Database:** Skip stories already summarized.
4. **Scrape Article Content:** Download article HTML.
5. **Summarize with LLM:** Use Docker Model Runner to generate a summary.
6. **Store Results:** Save metadata, content, and summary in PostgreSQL.

**Notes:**

- Uses the [Hacker News API](https://github.com/HackerNews/API) and Firebase client.
- Handles errors for unreachable or non-HTML URLs.
- All data is persisted in PostgreSQL (managed by Docker Compose).

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Docker Model Runner enabled.
- VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

### Verify Docker Model Runner

Check that Docker Model Runner is running:

```bash
docker model status
```

You should see output indicating it is running.

### Pull the Gemma 3 Model

Download the quantized Gemma 3 model:

```bash
docker model pull ai/gemma3:4B-Q4_K_M
```

## Development Environment

This project uses a VS Code dev container for a consistent Python development setup with Docker and PostgreSQL. The dev container:

- Installs Python, Docker CLI, Git, and GitHub CLI.
- Uses Docker Compose to run the app and PostgreSQL.
- Sets `MODEL_HOST` to `http://model-runner.docker.internal` for model access.

### Build and Run Dev Container

Open the VS Code Command Palette (`⇧⌘P` on macOS), select `DevContainers: Rebuild and Reopen in Container`.

### Test Docker Model Runner

Inside the dev container terminal, run:

```bash
curl $MODEL_HOST/models
```

You should see a JSON list of available models.

## Production Environment

Docker Model Runner provides OpenAI API Spec compliant endpoints, so you can point `MODEL_HOST` to a production inference server if needed. For this demo, we use the local Docker Model Runner endpoint.

### Build and Run the Demo

Clone the repository and start the containers:

```bash
cd hackernews-summary
docker compose up --build --exit-code-from app
```

The app will process stories and exit when done.

## Clean Up

Remove containers and models:

```bash
docker compose down --rmi all --volumes
docker model rm ai/gemma3:4B-Q4_K_M
```

## Additional Tips

- All required tools (`docker`, `git`, `gh`, `python3`, etc.) are pre-installed in the dev container.

## References

- [Docker Model Runner Documentation](https://docs.docker.com/model-runner/)
- [Hacker News API](https://github.com/HackerNews/API)
- [Gemma 3 Model on Docker Hub](https://hub.docker.com/layers/ai/gemma3/4B-Q4_K_M/images/sha256-0b329b335467cccf7aa219e8f5e1bd65e59b6dfa81cfa42fba2f8881268fbf82)

---

**Summary:**  
This project provides a clear, hands-on example of using Docker Model Runner to run LLMs in a reproducible, containerized environment. Follow the steps above to fetch, summarize, and store Hacker News stories using modern, enterprise-ready tooling.
