#!/usr/bin/python3
"""A fabric script that deploys web content to my servers."""

#  import statements
import os
from fabric.operations import put
from fabric.operations import sudo
from fabric.api import env

env.user = 'ubuntu'
env.hosts = ['107.23.107.130', '54.145.80.47']


def do_deploy(archive_path):
    """A function that performs the task of web content deployment.
        Args
            archive_path: A string that represents the path to web content
        Return:
            True: if the archive_path is valid and deployment is successfull
            False: if archive_path is invalid and deployment is unsuccessfull
    """
    try:
        if os.path.exists(archive_path):
            #  extracting the name of compressed file from the archive path
            ziped_file = archive_path.lstrip('versions/')
            sudo(' if ! test -d /tmp/ ; then mkdir /tmp/ ; fi')
            #  uploading content to server
            put(archive_path, f'/tmp/{ziped_file}')
            #  removed the .tgz extension of the ziped file
            unzip_name = ziped_file.rstrip('.tgz')
            unzip_loc = f'/data/web_static/releases/{unzip_name}'
            sudo(f'mkdir -p {unzip_loc}')
            #  uncompressing the archive
            sudo(f'tar -xzf /tmp/{ziped_file} -C {unzip_loc}')
            sudo(f'rm /tmp/{ziped_file}')
            #  moving the content of the web_static folder into parent folder
            sudo(f'mv {unzip_loc}/web_static/* {unzip_loc}')
            sudo(f'rm -rf {unzip_loc}/web_static')
            sudo('rm -rf /data/web_static/current')
            sudo(f'ln -s {unzip_loc} /data/web_static/current')
            print('Deployed successfully')
        else:
            return False
    except Exception as e:
        print(e)
        return False
