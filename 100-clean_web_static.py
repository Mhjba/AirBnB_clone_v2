#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["18.210.33.166", "100.26.250.24"]


def do_clean(number=0):
    """Delete old archive files.
    Args: number (int): The quantity of archives to be stored.
    Only the most recent archive is kept if number is 0 or 1.
    The most and second-most recent archives are kept if the number is 2, etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
