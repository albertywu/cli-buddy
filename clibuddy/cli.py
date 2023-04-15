import click
import os
import sys
import importlib.util
import subprocess


@click.command()
@click.option("--explain", is_flag=True, help="Explain any errors that occurred when the wrapped tool ran")
@click.option("--fix", is_flag=True, help="Attempt to fix any errors that occurred when the wrapped tool ran")
@click.argument("wrapped_command", nargs=-1)
def main(explain, fix, wrapped_command):
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
        click.echo(f"Tool not found: {tool_file}")
        sys.exit(1)

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
            explanation = tool_module.explain(stdout + stderr, returncode)
            click.echo(explanation)

        if fix:
            patch = tool_module.fix(stdout + stderr, returncode)
            click.echo(patch)

    sys.exit(returncode)


if __name__ == "__main__":
    main()
