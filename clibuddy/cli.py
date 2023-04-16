import click
import os
import sys
import importlib.util
import subprocess
from clibuddy.logger.log import setup_logger
from rich.live import Live
from rich.text import Text
from rich.panel import Panel
from rich import box

@click.command()
@click.option("--explain", is_flag=True, help="Explain any errors that occurred when the wrapped tool ran")
@click.option("--fix", is_flag=True, help="Attempt to fix any errors that occurred when the wrapped tool ran")
@click.option("--debug", is_flag=True, help="Enable debug mode.")
@click.argument("wrapped_command", nargs=-1)
def main(explain, fix, debug, wrapped_command):
    setup_logger(debug)

    if not explain and not fix:
        click.echo("Please provide at least one of --explain or --fix")
        sys.exit(1)

    if not wrapped_command:
        click.echo("Please provide a wrapped command to run")
        sys.exit(1)

    tool_name = wrapped_command[0]
    tools_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
    tool_file = os.path.join(tools_dir, f"{tool_name}.py")

    if not os.path.exists(tool_file):
        tool_file = os.path.join(tools_dir, "default.py")

    spec = importlib.util.spec_from_file_location("tool_module", tool_file)
    tool_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool_module)

    # Run the wrapped command and stream stdout and stderr to the main process
    wrapped_command_str = ' '.join(wrapped_command)
    process = subprocess.Popen(wrapped_command_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture and print stdout and stderr in real-time
    stdout, stderr = "", ""
    for line in iter(process.stdout.readline, ''):
        stdout += line
        click.echo(line, nl=False)
    for line in iter(process.stderr.readline, ''):
        stderr += line
        click.echo(line, nl=False, err=True)

    # Wait for the process to complete and get the return code
    returncode = process.wait()

    # Check if the wrapped command failed with an exit code > 0
    if returncode != 0:
        if explain:
            stream = tool_module.explain(wrapped_command_str, stdout + stderr, returncode)
            stream_to_console(stream)

        if fix:
            stream = tool_module.fix(wrapped_command_str, stdout + stderr, returncode)
            stream_to_console(stream)

    sys.exit(returncode)


def stream_to_console(stream):
    live_text = Text("", style="bold bright_cyan")
    panel = Panel(live_text, box=box.ROUNDED, expand=False, padding=(1, 2))

    with Live(panel) as panel:  # update 4 times a second to feel fluid
        panel.console.rule("CliBuddy", style="cyan")
        for chunk in stream:
            nxt = chunk["choices"][0].get("delta", {}).get("content")
            if nxt is not None:
                live_text.append(nxt)


if __name__ == "__main__":
    main()
