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


@cli.command('connect', short_help='Establish a connection to AWS')
@click.option('--username', '-u', prompt=True)
@click.option('--password', '-p', prompt=True, hide_input=True)
def connect(username, password):
    utils.establish_connection(username, password)


@cli.command('pull', short_help='Pull remote changes (auto fetches)')
def pull():
    utils.pull()


@cli.command('push', short_help='Push files to Git+AWS')
@click.option('--project', '-proj', prompt=True)
def push(project):
    utils.push(project)


@cli.command('status', short_help='Git Status')
def status():
    utils.status()

