import click
from eus import utils


@click.group()
def cli():
    """Welcome to the EUS CLI!
    """


@cli.command('add', short_help='Add files to staging')
@click.argument('filename', default='.')
def add(filename):
    utils.add(filename)


@cli.command('commit', short_help='Commit files locally')
@click.option('--message', '-m', prompt=True)
def commit(message):
    utils.commit(message)


@cli.command('pull', short_help='Pull remote changes (auto fetches)')
def pull():
    utils.pull()


@cli.command('push', short_help='Push files to Git+AWS')
@click.option('--username', '-u', prompt=True)
@click.option('--password', '-pwd', prompt=True, hide_input=True)
@click.option('--project', '-proj', prompt=True)
def push(username, password, project):
    utils.push(username, password, project)

