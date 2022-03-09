import os
import paramiko
from dotenv import load_dotenv


load_dotenv()
ADDRESS = os.environ.get("cluster_adress") 
USERNAME = os.environ.get("ssh_username") 
# KEY = os.environ.get("ssh_password") 
# ROOT_PASSORD = os.environ.get("ROOT_PASSORD") 


def get_config() -> bool:
    print("CONFIGURE")
    
    sk_dc = os.path.dirname(__file__)
    kube_config = os.path.join(sk_dc, 'kube_config')
    if not os.path.exists(kube_config): os.mkdir(kube_config)

    localpath = 'config'
    remotepath = '/home/ec2-user/.kube/config'

    os.chdir(kube_config)
    print('Changed directory')

    ssh = paramiko.SSHClient()

    try:
        print('Connecting to {}'.format(ADDRESS))
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('Policy set')

        ssh.connect(ADDRESS, username=USERNAME, key_filename='/home/centos/.ssh/id_rsa')
        print('Connected')

        sftp = ssh.open_sftp()
        print('SFTP opened')

        sftp.get(remotepath, localpath)
        print('CONFIG downloaded')

        sftp.close()
        ssh.close()
        print('Connection closed')


    except Exception as e:
        print(f'Procedure failed/n{e}')


    

