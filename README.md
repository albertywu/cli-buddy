## cli-buddy

Wrap your CLI's with an AI buddy that can explain and fix failures.

## Build Prompt (GPT-4)

I want to create a python CLI tool called 'clibuddy' that uses the 'click' library.

The CLI tool will wrap another command, and will either 1) print out detailed information of what failed or 2) attempt to fix errors any time the wrapped command fails with exit code > 0.

Structure of CLI app:
```
clibuddy --tool="tools/mytool.py" --explain mytool ...mytool_args
clibuddy --tool="tools/mytool.py" --fix mytool ...mytool_args
```

---

Concrete examples:

1) `clibuddy --tool="tools/yarn.py" --explain yarn run test`

Runs `yarn run test` and explains any errors that occured. Uses the explain function in tools/yarn.py to write the explanation to STDOUT if `yarn run test` failed. If "yarn run test" did not fail, then output no additional information. Make sure to always propagate STDOUT / STDERR of the wrapped command.

2) `clibuddy --tool="tools/yarn.py" --fix yarn run test`

Runs `yarn run test` and attempts to fix any errors that occured in the source code by producing a git patch with the fix and outputting it to stdout. Uses the fix function in tools/yarn.py to produce the fix output (a git patch string with the fix). If the wrapped command `yarn run test` did not fail, then do nothing.

3) `clibuddy --tool="tools/yarn.py" --explain --fix yarn run test`

Does both 1) and 2)

---

A tool will automatically be read from the file tools/<tool>.py
Each <tool>.py file contains the following two functions, based on the underlying command that was invoked.

```python
def explain(log: str, exitcode: int) -> str:
  ...

def fix(log: str, exitcode: int) -> str
  ...
```

Please implement the scaffolding for this python application.