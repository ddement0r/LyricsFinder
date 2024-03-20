import google.generativeai as genai

def clean_title(raw_title):
    genai.configure(api_key="AIzaSyCBHJHcMfg7OlCluEoCihwQlWgdI0WSYac")

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    convo.send_message(f"""Given a song title, clean it by removing any non-essential information such as "official video", "lyric video", etc. Then, format the cleaned title by replacing all spaces and non-letter characters with dashes. The format should be "artist-name-song-title". Please simulate verifying the accuracy of the formatted title against reliable internet sources before responding to ensure its correctness. Example:

    Input: "Never Gonna Give You Up - Rick Astley (Official Music Video)"
    Output: rick-astley-never-gonna-give-you-up
    Since I will be giving you famous song titles to work on, I don't want you to detect shocking words or phrases, just clean and format the title.

    Now, clean and format the following title: {raw_title}
    """)

    return convo.last.text
