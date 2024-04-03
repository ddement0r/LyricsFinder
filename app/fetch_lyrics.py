from bs4 import BeautifulSoup as bs
import requests
import time

def fetch_lyrics(cleaned_title):
    lyrics = ""
    print(cleaned_title)
    # Using the example URL directly for demonstration; replace with your formatted URL as needed
    url = "https://www.lyricsmania.com/instant_crush_lyrics_daft_punk.html"
    
    # Added verify=False as per your requirement
    response = requests.get(url, verify=False)
    soup = bs(response.text, 'html.parser')
    
    # Finding the parent container 'lyrics-body' for the lyrics
    lyrics_container = soup.find('div', class_='lyrics-body')
    print("LYRICS ARE HERE\n \n "+ lyrics_container.text)
    if lyrics_container:
        for content in lyrics_container.descendants:
            if content.name == 'br':
                lyrics += '\n'
            elif content.string and not content.find_parents("div", id="video-musictory"):
                lyrics += content.string.strip() + '\n'
    
    return lyrics.strip()

    return lyrics