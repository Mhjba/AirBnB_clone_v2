#!/usr/bin/python3
""" module for web application deployment with Fabric."""

from fabric.api import run, put, env, local
from os.path import exists
from os.path import isdir
from datetime import datetime

env.hosts = ["54.235.193.23", "	54.209.125.126"]


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
    """Deploys the static files to the host servers"""
    if exists(archive_path) is False:
        return False
    try:
        f_path = archive_path.split("/")[-1]
        file_name = f_path.split(".")[0]
        dol_path = "/data/web_static/releases/"
        put(archive_path, f"/tmp/")
        run(f"mkdir -p {dol_path}/{file_name}")
        run(f"tar -xzf /tmp/{f_path} -C {dol_path}/{file_name}/")
        run(f"rm /tmp/{f_path}")
        run(f'mv {dol_path}/{file_name}/web_static/* {dol_path}/{file_name}/')
        run(f'rm -rf {dol_path}/{file_name}/web_static')
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {dol_path}/{file_name}/ /data/web_static/current")
        return True
    except Exception:
        return False
