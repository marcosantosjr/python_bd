import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "http://quotes.toscrape.com/"

# Fetch the HTML content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
else:
    print(f"Failed to fetch page: {response.status_code}")

# Extract all quote blocks
quotes_data = []
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    quotes_data.append({"quote": text, "author": author})

# Display the first 5 quotes
for item in quotes_data[:5]:
    print(f"{item['quote']} - {item['author']}")


# Convert to a DataFrame and save to CSV
df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)

print("Quotes saved to quotes.csv")

# Count unique authors
unique_authors = df['author'].nunique()
print(f"Number of unique authors: {unique_authors}")

# Function to scrape a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    page_data = []
    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)
        page_data.append({"quote": text, "author": author})
    return page_data

# Scrape all pages
base_url = "http://quotes.toscrape.com"
all_quotes = []
page = 1

while True:
    print(f"Scraping page {page}...")
    page_url = f"{base_url}/page/{page}/"
    response = requests.get(page_url)
    if "No quotes found!" in response.text:
        break
    all_quotes.extend(scrape_page(page_url))
    page += 1

# Save all quotes to a CSV
df_all = pd.DataFrame(all_quotes)
df_all.to_csv("all_quotes.csv", index=False)
print(f"Scraped {len(all_quotes)} quotes across {page-1} pages.")
