from clibuddy.format.text_format import red, blue


def explain(log: str, exitcode: int) -> str:
    return blue(f"Explanation for bazel error: log='{log}', exitcode={exitcode}")


def fix(log: str, exitcode: int) -> str:
    return red(f"Fix for bazel error: log='{log}', exitcode={exitcode}")

