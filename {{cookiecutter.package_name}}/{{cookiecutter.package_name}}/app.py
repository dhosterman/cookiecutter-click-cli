import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.command(context_settings=CONTEXT_SETTINGS)
def main():
    """Entry point for the application."""
    click.echo("Hello, world!")
