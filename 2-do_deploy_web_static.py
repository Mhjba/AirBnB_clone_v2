#!/usr/bin/python3
'''
    Deploy web_static on Servers
'''
from fabric.api import run, put, env, local
from os.path import exists
from datetime import datetime

env.hosts = ["54.235.193.23", "	54.209.125.126"]


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
