import openai
from .config import ENGINE, MAX_TOKENS, TEMPERATURE

class GPT:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def ask(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who is an expert at coding."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content'].strip()