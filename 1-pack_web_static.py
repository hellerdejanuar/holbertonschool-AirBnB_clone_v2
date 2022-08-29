#!/usr/bin/env bash
""" generates a .tgz archive from the contents of the web_static folder """
from datetime import datetime
from fabric.operations import local

def do_pack():
    local('mkdir -p versions')
    tarball_path = 'versions/web_static_' + datetime.now().strftime(%Y%m%d%H%M%S) + '.tgz'
    tarball = local('tar -czvf {} web_static'.format(tarball_path), capture=True)

    return tarball if not tarball.failed else None
