import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

quotes = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for page in range(1, 6):
    url = f"https://quotes.toscrape.com/page/{page}/"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "lxml")

    for q in soup.select(".quote"):
        text = q.select_one(".text")
        author = q.select_one(".author")
        tags = q.select(".tag")

        quotes.append({
            "quote": text.get_text(strip=True) if text else "",
            "author": author.get_text(strip=True) if author else "",
            "tags": "|".join([t.get_text(strip=True) for t in tags])
        })

    time.sleep(1)

df = pd.DataFrame(quotes)
df.to_csv("quotes.csv", index=False)

print("Scraping Finished!!!")