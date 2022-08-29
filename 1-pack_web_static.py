#!/usr/bin/python3
""" fabric deploy module  """
from datetime import datetime
from fabric.operations import local


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
