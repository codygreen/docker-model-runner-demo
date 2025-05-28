import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Attempt to extract readable content
        paragraphs = soup.find_all("p")
        content = "\n".join(p.get_text() for p in paragraphs)
        return content.strip()
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
