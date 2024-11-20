import click


@click.group(short_help="custom_validation CLI.")
def custom_validation():
    """custom_validation CLI.
    """
    pass


@custom_validation.command()
@click.argument("name", default="custom_validation")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [custom_validation]
