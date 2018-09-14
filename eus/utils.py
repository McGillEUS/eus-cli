import ctypes
import logging
import os
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from subprocess import run

server = 'gastly.mcgilleus.ca'
port = ''


def _generic_runner(command, message=""):
    split_command = command.split(' ')
    if message:
        split_command.append(message)
    run(split_command)


"""The following commands run Git commands as-is
"""
def add(filename):
    command = f'git add {filename}'
    _generic_runner(command)


def commit(message):
    command = 'git commit -m'
    _generic_runner(command, message)


def fetch():
    command = f'git fetch'
    _generic_runner(command)


def pull():
    fetch()
    command = 'git pull'
    _generic_runner(command)


def push(deploy=False):
    """Pushes to Git, and if specified AWS as well.

    Arguments:
        - deploy: Whether or not to deploy to AWS
    """
    command = 'git push'
    _generic_runner(command)

    if deploy:
        folder = os.getcwd()
        logging.info(f"Deploying the contents of {folder} to {global_project}")
        deploy(folder)


def deploy(folder, project=None, username=None, password=None):
    if not username and not password or not project:
        logging.error("Make sure your username, password, and project are set.")
        return

    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(server, username=username, password=password)
    with SCPClient(ssh_client.get_transport()) as scp_client:
        scp_client.put(folder, f'/srv/www/{project}/', recursive=True)


def setup_environment(username, password, project):
    """Sets up global variables for dealing with AWS.

    Arguments:
        - username: The user's AWS username
        - password: The user's AWS password
        - project: The default project to deploy to
    """
    os.environ['server_credentials'] = username+" "+ password
    os.environ['default_project'] = project


def status():
    command = 'git status'
    _generic_runner(command)

