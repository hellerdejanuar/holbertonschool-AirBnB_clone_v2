#!/usr/bin/env bash
""" generates a .tgz archive from the contents of the web_static folder """
from datetime import datetime

def do_pack():
    filename = 'web_static_' + datetime.now().strftime(<%Y><%m><%d><%H><%M><%S>) + '.tgz'
    local(f'tar -czvf {filename}')
