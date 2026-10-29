import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def generate_haiku(topic: str) -> str:
    parameterized_prompt = (
        f"Write a haiku about the topic '{topic}']."
        f"The poem must strictly follow the traditional 5-7-5 syllable structure. "
        f"Line 1 must have exactly 5 syllables, line 2 must have exactly 7 syllables, "
        f"and line 3 must have exactly 5 syllables. "
        f"Return ONLY the three distinct lines of poetry with no introductory text, notes, or markdown."
    )
    
    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": parameterized_prompt}
        ],
        max_tokens=200,
        temperature=0.0
    )
    
    try:
        haiku_text = response.choices[0].message.content.strip()
    except (TypeError, AttributeError):
        choice = response['choices'][0] if isinstance(response, dict) else response.choices[0]
        if isinstance(choice, dict):
            haiku_text = choice['message']['content'].strip()
        else:
            haiku_text = choice.message.content.strip()
            
    return haiku_text

if __name__ == "__main__":
    current_topic = "sky"
    haiku_output = generate_haiku(current_topic)
    print(haiku_output)
