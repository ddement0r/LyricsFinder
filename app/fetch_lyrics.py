from bs4 import BeautifulSoup as bs
import requests

def fetch_lyrics(cleaned_title):
    lyrics = ""
    print(cleaned_title)
    url = f"https://www.lyricsmania.com/{cleaned_title}.html"
    
    response = requests.get(url, verify=False)
    soup = bs(response.text, 'html.parser')
    
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