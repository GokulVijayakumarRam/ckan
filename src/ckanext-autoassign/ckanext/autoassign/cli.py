import click


@click.group(short_help="autoassign CLI.")
def autoassign():
    """autoassign CLI.
    """
    pass


@autoassign.command()
@click.argument("name", default="autoassign")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [autoassign]
