import click

@click.group()
def cli():
    """Welcome to the EUS CLI!
    """


@cli.command('add', short_help='Add files to staging')
def add():
    pass


@cli.command('commit', short_help='Commit files locally')
def commit():
    pass


@cli.command('pull', short_help='Pull remote changes')
def pull():
    pass


@cli.command('push', short_help='Push files to Git+AWS')
def push():
    pass

