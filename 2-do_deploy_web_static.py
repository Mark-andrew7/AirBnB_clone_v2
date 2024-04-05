#!/usr/bin/python3
# Distrubutes archive to my web servers

from os import path
from fabric.api import env, put, run

env.hosts = ['52.91.150.164', '18.204.16.72']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    distributes archive to web servers
    """
    try:
        if not path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')
        archive_filename = path.basename(archive_path)
        release_dir = "/data/web_static/releases/{}".format(
            archive_filename.split('0')[0])
        run('mkdir -p {}'.format(release_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_dir))

        run('rm /tmp/{}'.format(archive_filename))
        extracted_dir = "{}/web_static".format(release_dir)
        run("mv {}/web_static/* {}".format(extracted_dir, release_dir))

        run("rm -rf {}/web_static".format(release_dir))
        run("rm -rf /data/web_static/current")
        return True
    except:
        return False
