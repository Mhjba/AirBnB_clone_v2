#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from os.path import isdir
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ["34.73.0.174", "35.196.78.105"]
"""The list of host server IP addresses."""


@runs_once
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
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
