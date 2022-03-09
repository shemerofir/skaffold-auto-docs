import sh
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.environ.get("sudo_password") 


def get_docker():
    with sh.contrib.sudo(password=PASSWORD, _with=True):

        print('yum-utils')
        sh.yum ('-y', 'install', 'yum-utils')

        print('add-repo')       
        sh.sudo('yum-config-manager', '--add-repo', 'https://download.docker.com/linux/centos/docker-ce.repo')

        print('docker-ce')
        sh.yum('install', 'docker-ce', 'docker-ce-cli', 'containerd.io', '-y')

        print('enable')
        sh.systemctl('enable', 'docker')

        print('start')
        sh.systemctl('start', 'docker')
