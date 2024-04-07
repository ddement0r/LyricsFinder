from bs4 import BeautifulSoup as bs, Comment
import requests
import certifi


def fetch_lyrics(cleaned_title):
    lyrics = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url = f"https://b.azlyrics.com/lyrics/{cleaned_title}.html"

    response = requests.get(url, verify=certifi.where(), headers=headers)
    soup = bs(response.text, "html.parser")

    classes_to_remove = [
        "div-share noprint",
        "div-share",
        "lyricsh",
        "ringtone",
        "noprint",
        "smt noprint",
        "smt",
        "abovebreadcrumb noprint",
        "panel songlist-panel noprint",
        "feat",
    ]
    for class_to_remove in classes_to_remove:
        for div in soup.find_all("div", class_=class_to_remove):
            div.extract()
    for span in soup.find_all("span", class_="feat"):
        span.decompose()

    for b in soup.find_all("b"):
        b.extract()

    for ol in soup.find_all("ol"):
        ol.extract()

    for form in soup.find_all("form"):
        form.extract()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    divs = soup.find_all("div", class_="col-xs-12 col-lg-8 text-center")
    for div in divs:
        for content in div.descendants:
            if content.name == "br":
                lyrics += "\n"
            elif content.string and not content.find_parents(
                "div", id="video-musictory"
            ):
                lyrics += content.string.strip()
        break
    nice_lyrics = lyrics.strip()
    print(nice_lyrics)

    return nice_lyrics
