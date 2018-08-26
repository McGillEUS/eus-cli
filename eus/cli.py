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


@cli.command('setup', short_help='Set up the credentials and project'
                                 'you wish to deploy to by default.')
@click.option('--username', '-usr', prompt=True)
@click.option('--password', '-pwd', prompt=True, hide_input=True)
@click.option('--project', '-proj', prompt=True)
def setup(username, password, project):
    utils.setup_environment(username, password, project)


@cli.command('deploy', short_help='Deploys a folder to a project on Gastly')
@click.option('--source', '-src', prompt=True)
@click.option('--destination', '-dest', default=None)
def deploy(source, destination):
    utils.deploy(source, destination)


@cli.command('pull', short_help='Pull remote changes (auto fetches)')
def pull():
    utils.pull()


@cli.command('push', short_help='Push files to Git+AWS')
@click.option('--deploy', '-dply', is_flag=True)
def push(deploy):
    utils.push(deploy)


@cli.command('status', short_help='Git Status')
def status():
    utils.status()

