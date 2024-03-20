from bs4 import BeautifulSoup as bs
import requests
import time

def fetch_lyrics(cleaned_title):
    lyrics = ""
    print(cleaned_title)
    url = f"https://genius.com/{cleaned_title}-lyrics"
    # time.sleep(20)
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    lyrics_container = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
    lyrics = ""
    if lyrics_container:
        for div in lyrics_container:
            if div != 'span':
                lyrics += div.text + ' '
            elif div == 'span' or div == 'a':
                lyrics += div.get_text() + ' '
    else:
        lyrics = "Lyrics not found."
    return lyrics
