

def explain(log: str, exitcode: int) -> str:
    return f"Explanation for bazel error: log='{log}', exitcode={exitcode}"


def fix(log: str, exitcode: int) -> str:
    return f"Fix for bazel error: log='{log}', exitcode={exitcode}"

