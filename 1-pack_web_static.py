#!/usr/bin/python3
'''
    Fabric script that generates a .tgz archive from
    the contents of the web_static folder
'''
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' pack the contents of web_static folder '''
    current_date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_" + current_date + ".tgz"

    local("mkdir -p versions")
    folder_path = f"versions/{archive_name}"
    try:
        local(f"tar -cvzf {folder_path} web_static")
        return folder_path
    except Exception:
        return None
