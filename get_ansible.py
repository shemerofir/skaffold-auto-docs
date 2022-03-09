import sh
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.environ.get("sudo_password") 

def get_ansible():
    with sh.contrib.sudo(password=PASSWORD, _with=True):

        print('Downloading epel-release')
        sh.yum('install', 'epel-release', '-y')

        print('Downloading Ansible')
        sh.yum('install', 'ansible', '-y')
