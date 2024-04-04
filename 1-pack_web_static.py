#!/usr/bin/python3
#  generates a .tgz archive from the contents of the web_static

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create archive
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))

    if result:
        return archive
    else:
        return None
