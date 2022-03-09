import sh
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.environ.get("sudo_password") 


def get_minikube():
    with sh.contrib.sudo(password=PASSWORD, _with=True):

        print('Downloading Minikube')
        sh.curl('-LO', 'https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64')
        
        print('Installing Minikube')
        sh.install('minikube-linux-amd64', '/usr/local/bin/minikube')
