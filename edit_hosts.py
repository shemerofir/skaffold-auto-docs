import socket
import sh
from dotenv import load_dotenv
import os


load_dotenv()
PASSWORD = os.environ.get("sudo_password") 


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

def edit_hosts():
    print('Edit /etc/hosts')
    with sh.contrib.sudo(password=PASSWORD, _with=True):
        # with open('/etc/hosts', 'a') as f:
        #     f.writelines(f'{local_ip} devrepo\n')
        sh.echo(f'{local_ip} devrepo', '-n', '>>', '/etc/hosts')
        sh.cat('/etc/hosts')
