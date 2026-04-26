import os
from dotenv import load_dotenv
from groq import Groq
import json

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=api_key)


def extract_data(text):
    prompt = f"""
    Extract:
    hcp_name, topic, follow_up
    from: {text}
    Return JSON only
    """

    res = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        return json.loads(res.choices[0].message.content)
    except:
        return {
            "hcp_name": "Unknown",
            "topic": text,
            "follow_up": ""
        }
