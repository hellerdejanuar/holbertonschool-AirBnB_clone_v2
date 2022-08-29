#!/usr/bin/python3
""" fabric deploy module  """
from datetime import datetime
from fabric.operations import local, run, put
from fabric.api import env
from os import path

env.hosts = ['34.227.46.143', '18.234.112.14']


def do_pack():
    """ Compress a directory """

    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_path = 'versions/web_static_' + now + '.tgz'
    tarball = local('tar -czvf {} web_static'.format(tar_path), capture=True)
    if tarball.failed:
        return None
    else:
        return tarball

def deploy(archive_path):
    """ distributes file to servers specified in env.hosts """

    code_dir='/data/web_static/releases/{}'.format()

    if not archive_path:
        return False
    
    pack = do_pack()
    if pack.failed:
        return False

    
    

