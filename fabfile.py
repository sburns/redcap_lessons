from time import sleep
from fabric.api import local


def gen_css():
    local('sass my_ribbon/css/screen.scss:my_ribbon/css/screen.css')


def gen():
    local('landslide talk.cfg')


def loop(pause=2):
    while(True):
        gen()
        sleep(pause)


def deploy():
    local('rsync -a ./ eave:/var/www/html/talks/redcap_lessons/')


def open():
    local('open index.html')


def rebuild():
    gen_css()
    gen()
    deploy()
    open()