#!/usr/bin/python3
"""A fabric script that archives a file in preparation of deployment."""
from fabric.operations import local


def do_pack():
    """A function that performs the task of archiving and compressing
        a web directory.
    """
    #  creating a directory to store archived files
    local('if ! test -d versions; then  mkdir versions ; fi')
    result = local('date +"%Y%m%d%H%M%S" ', capture=True)
    date = result.stdout.strip()
    filename = f'web_static_{date}'
    extension = '.tgz'
    fullname = f'{filename}{extension}'
    outcome = local(f'tar -cvzf versions/{fullname} web_static', capture=True)
    if outcome.succeeded:
        return f'versions/{fullname}'
    else:
        return None
