import sh
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.environ.get("sudo_password") 


def get_skaffold():
    with sh.contrib.sudo(password=PASSWORD, _with=True):
        print('Installin Skaffold')
        sh.curl('-Lo',
                'skaffold',
                'https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64')
        sh.install('skaffold', '/usr/local/bin/')
