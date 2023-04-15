import os
from clibuddy.llm.gpt import GPT
from clibuddy.logger.log import logger

api_key = os.getenv("OPENAI_API_KEY")
gpt = GPT(api_key)

def explain(command: str, log: str, exitcode: int) -> str:
    prompt = f"""
I ran this git cli command in my terminal and got a non-zero exitcode {exitcode}:

{command}

Please help explain what went wrong. Here is the full error log:

{log}
    """
    logger.debug(prompt)
    response = gpt.ask(prompt)
    return response


def fix(command: str, log: str, exitcode: int) -> str:
    prompt = f"""
I ran this git cli command in my terminal and got a non-zero exitcode {exitcode}:

{command}

Use information about the command, exitcode, and the logs below to generate a git patchfile that I can apply using the "git apply" command.
Just reply with the git patch file and nothing else.

--- logs are below ---

{log}
    """
    logger.debug(prompt)
    response = gpt.ask(prompt)
    return response

