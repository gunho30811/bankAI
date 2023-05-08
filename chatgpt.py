import openai
import os
os.environ["OPENAI_API_KEY"] = "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"
# Replace with your API key
openai.api_key= os.environ["OPENAI_API_KEY"]

def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer