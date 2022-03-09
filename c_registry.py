import sh
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.environ.get("sudo_password") 


def c_registry():
    with sh.contrib.sudo(password=PASSWORD, _with=True):
        sh.docker('run', '-d', '-p', '5000:5000', '--restart=always', '--name', 'registry', 'registry:2')
