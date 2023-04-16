import openai
from openai.openai_response import OpenAIResponse
from typing import Iterator


class GPT:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def ask(self, prompt: str) -> Iterator[OpenAIResponse]:
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who is an expert at coding."},
                {"role": "user", "content": prompt},
            ],
            stream=True
        )