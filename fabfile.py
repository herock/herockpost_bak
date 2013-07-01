# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *
# from fabric.contrib.console import confirm

env.roledefs = {
    # 'test': ['herock@192.168.1.108'],
    'product': ['root@192.155.83.165:2213']
}

# APPS = ('bidding', 'bidding')

# TEST_SERVER_DIR = '/home/herock/ENV_appsku/appsku'
PRODUCT_SERVER_DIR = '/home/imom0/www/herockpost/blog/herockpost'


# workflow local

def release():
    """ 发布到github """
    push('master')


def push(branch='master'):
    local('git push origin %s' % branch)


# workflow remote

@roles('product')
def deploy_blog():
    """ 在产品服务器上部署新版本 """
    release()
    with cd(PRODUCT_SERVER_DIR):
        get_latest_version()
    restart_nginx()


# functions remote
def get_latest_version(branch='master'):
    """ 在远程服务器pull最新代码，并安装依赖与migarate数据库 """
    run('git pull origin %s' % branch)


def restart_nginx():
    sudo('nginx -s stop')
    sudo("/etc/rc.d/nginx start")
