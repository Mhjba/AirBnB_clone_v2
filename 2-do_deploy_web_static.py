#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from os.path import isdir, exists 
from fabric.api import env, local, put, run


env.hosts = ["54.172.176.21", "54.234.38.223"]
"""The list of host server IP addresses."""


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


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        return True
    except Exception:
        return False
