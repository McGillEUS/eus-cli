import logging
import os
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from subprocess import run

server = 'gastly.mcgilleus.ca'
global_username = ''
global_password = ''
default_project = ''
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


def deploy(folder, project=None):
    if not global_username and not global_password or not default_project:
        logging.error("Make sure your username, password, and default project are set. "
                      "Please run `eus setup` for more information")
        return

    if not project:
        logging.warning(f"Project not specified. Defaulting to {default_project}")
        project = default_project

    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(server, username=global_username, password=global_password)
    with SCPClient(ssh_client.get_transport()) as scp_client:
        scp_client.put(folder, f'/srv/www/{project}/')


def setup_environment(username, password, project):
    """Sets up global variables for dealing with AWS.

    Arguments:
        - username: The user's AWS username
        - password: The user's AWS password
        - project: The default project to deploy to
    """
    global_username = username
    global_password = password
    default_project = project


def status():
    command = 'git status'
    _generic_runner(command)

