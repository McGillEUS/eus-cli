from subprocess import run

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


def push(username, password,  project):
    """Push uses the common Git utility + deploys to AWS.
    
    Arguments:
        - username: The user's AWS username
        - password: The user's AWS password
        - project: The EUS project within AWS. It requires to be part of `/srv/www`.
    """
    command = 'git push'
    _generic_runner(command)
    # TODO: [aungur] add logic to push to AWS


def status():
    command = 'git status'
    _generic_runner(command)

