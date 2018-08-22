import logging
from subprocess import run
from paramiko import SSHClient
from scp import SCPClient

server = 'gastly.mcgilleus.ca'
port = ''
scp_global = None


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


def push(project, folder='.'):
    """Pushes to Git + AWS

    Arguments:
        - project: Project within `/srv/www` on Gastly
        - folder: Folder containing files to be deployed to Gastly
    """
    command = 'git push'
    _generic_runner(command)
    logging.warning(f"Transferring {folder} to {server}:/srv/www/{project}")
    scp_global.put(folder, recursive=True, remote_path=f'/srv/www/{project}')


def establish_ssh_connection(username, password):
    """Establishes the SSH connection to Gastly to allow SCP.

    Arguments:
        - username: The user's AWS username
        - password: The user's AWS password
    """
    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server, port, username, password)
    # Set the global variable for SCP'ing if the ssh initialization was successful
    if ssh_client:
        scp_global = SCPClient(ssh_client.get_transport())


def status():
    command = 'git status'
    _generic_runner(command)

