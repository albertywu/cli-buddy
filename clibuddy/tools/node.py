from clibuddy.format.text_format import red, blue


def explain(log: str, exitcode: int) -> str:
    return blue("\nTODO: call OPENAI api with this prompt string to explain the error")


def fix(log: str, exitcode: int) -> str:
    return red("\nTODO: call OPENAI api with this prompt string to fix the error")

