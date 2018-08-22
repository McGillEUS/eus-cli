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
    command = f'git pull'
    _generic_runner(command)


def push(project, credentials):
    """Push requires extra logic to deal with AWS
    """
    pass

