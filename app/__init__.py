from flask import Flask, request, jsonify
from .gemini_cleaning import clean_title
from .fetch_lyrics import fetch_lyrics

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/search_lyrics', methods=['POST'])
def search_lyrics():
    data = request.json
    raw_title = data.get('raw_title')
    cleaned_title = "tameimpala/thelessiknowthebetter"
    # cleaned_title = clean_title(raw_title)
    lyrics = fetch_lyrics(cleaned_title)
    return jsonify({'cleaned_title': cleaned_title, 'lyrics': lyrics})