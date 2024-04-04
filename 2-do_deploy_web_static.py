#!/usr/bin/python3
'''
    Deploy web_static on Servers
'''
from fabric.api import run, put, env, local
from os.path import exists
from datetime import datetime
from os.path import isdir

env.hosts = ["52.55.249.213", "	54.157.32.137"]


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
    ''' deploy archive to servers '''
    if exists(archive_path) is False:
        return False
    try:
        file_path = archive_path.split("/")[-1]
        file_name = file_path.split(".")[0]
        des_path = "/data/web_static/releases/"
        put(archive_path, f"/tmp/")
        run(f"mkdir -p {des_path}/{file_name}")
        run(f"tar -xzf /tmp/{file_path} -C {des_path}/{file_name}/")
        run(f"rm /tmp/{file_path}")
        run(f'mv {des_path}/{file_name}/web_static/* {des_path}/{file_name}/')
        run(f'rm -rf {des_path}/{file_name}/web_static')
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {des_path}/{file_name}/ /data/web_static/current")
        return True
    except Exception:
        return False
