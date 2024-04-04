#!/usr/bin/python3
""" module for web application deployment with Fabric."""

from os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    """Archives the static files_name"""
    dat_t = datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dat_t.year,
        dat_t.month,
        dat_t.day,
        dat_t.hour,
        dat_t.minute,
        dat_t.second)

    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return
