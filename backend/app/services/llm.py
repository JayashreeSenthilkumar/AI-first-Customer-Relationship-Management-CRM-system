from groq import Groq
import json

client = Groq(api_key="YOUR_GROQ_API_KEY")

def extract_interaction_data(text: str):
    prompt = f"""
    Extract structured CRM interaction data from the text.

    Text: "{text}"

    Return JSON only with:
    - hcp_name
    - topic
    - follow_up

    Example:
    {{
      "hcp_name": "Dr. Ravi",
      "topic": "diabetes discussion",
      "follow_up": "next week"
    }}
    """

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    try:
        return json.loads(output)
    except:
        # fallback if LLM returns messy text
        return {
            "hcp_name": "Unknown",
            "topic": text,
            "follow_up": None
        }
