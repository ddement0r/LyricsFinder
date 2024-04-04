from bs4 import BeautifulSoup as bs
import requests
import certifi

def fetch_lyrics(cleaned_title):
    lyrics = ""
    url = f"https://www.lyricsmania.com/{cleaned_title}.html"
    
    response = requests.get(url, verify=certifi.where())
    soup = bs(response.text, 'html.parser')
    
    video_div = soup.find('div', id='video-musictory')
    if video_div:
        video_div.extract()

    lyrics_container = soup.find('div', class_='lyrics-body')

    if lyrics_container:
        for content in lyrics_container.descendants:
            if content.name == 'br':
                lyrics += '\n'
            elif content.string and not content.find_parents("div", id="video-musictory"):
                lyrics += content.string.strip()
    nice_lyrics = lyrics
    print('\n' + nice_lyrics)

    return nice_lyrics