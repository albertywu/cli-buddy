import os
from clibuddy.llm.gpt import GPT
from clibuddy.logger.log import logger
from openai.openai_response import OpenAIResponse
from typing import Iterator

api_key = os.getenv("OPENAI_API_KEY")
gpt = GPT(api_key)


def explain(command: str, log: str, exitcode: int) -> Iterator[OpenAIResponse]:
    prompt = f"""
I ran this bazel cli command in my terminal and got a non-zero exitcode {exitcode}:

{command}

Please help explain what went wrong. Here is the full error log:

{log}
    """
    logger.debug(prompt)
    return gpt.ask(prompt)


def fix(command: str, log: str, exitcode: int) -> Iterator[OpenAIResponse]:
    prompt = f"""
I ran this bazel cli command in my terminal and got a non-zero exitcode {exitcode}:

{command}

Use information about the command, exitcode, and the logs below to generate a git patchfile that I can apply using the "git apply" command.
Just reply with the git patch file and nothing else.

--- logs are below ---

{log}
    """
    logger.debug(prompt)
    return gpt.ask(prompt)

