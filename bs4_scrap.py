import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Step 1: Scrape text from a website
URL = "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm"  # Pride and Prejudice (Public Domain)
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all paragraph text
    paragraphs = soup.find_all('p')
    text = " ".join([p.get_text() for p in paragraphs])

    # Step 2: Clean the text
    words_to_exclude = ["Mr", "Mrs", "said", "one", "upon", "could"]
    for word in words_to_exclude:
        text = text.replace(word, "")

    # Step 3: Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

else:
    print("Failed to retrieve the webpage.")

wordcloud.to_file("wordcloud_output.png")

WordCloud(max_words=100)
