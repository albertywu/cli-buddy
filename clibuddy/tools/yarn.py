from clibuddy.format.text_format import red, blue


def explain(log: str, exitcode: int) -> str:
    return blue(f"Explanation for yarn error: log='{log}', exitcode={exitcode}")


def fix(log: str, exitcode: int) -> str:
    return red(f"Fix for yarn error: log='{log}', exitcode={exitcode}")

