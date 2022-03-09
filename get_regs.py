import os
import paramiko
import yaml
from dotenv import load_dotenv


load_dotenv()
ADDRESS = os.environ.get("cluster_adress") 
USERNAME = os.environ.get("ssh_username") 
# KEY = os.environ.get("ssh_password") 

# def ssh_interact(u, a):
#     import sh

#     my_server = sh.ssh.bake(f"{u}@{a}")
#     my_server.sudo.mv('/home/ec2-user/registries.yaml', '/etc/rancher/rke2/registries.yaml')



def get_registries() -> bool:
    print("REGS")

    sk_dc = os.path.dirname(__file__)
    kube_config = os.path.join(sk_dc, 'kube_config')
    if not os.path.exists(kube_config): os.mkdir(kube_config)

    localpath = 'registries.yaml'
    remotepath = '/etc/rancher/rke2/registries.yaml'
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
        print('REGS downloaded')
        
        with open(r'registries.yaml') as file:
            documents = yaml.full_load(file)
        
        documents['mirros']['devrepo:5000'] = {'endpoint': ['https://devrepo:5000']}
        print("dump")
        with open(r'registries.yaml', 'w') as file:
            documents = yaml.dump(documents, file)
        print("dump done")
        sftp.put(localpath, remotepath)
        print('CONFIG uploaded')
        

        sftp.close()
        ssh.close()
        print('Connection closed')
        
        # import sh
        # from time import sleep
        
        # sleep(5)
        # sh.sudo.mv('/home/ec2-user/registries.yaml', '/etc/rancher/rke2/registries.yaml')
        #sh_interact(USERNAME, ADDRESS)
        print('EXCHANGED')


    except Exception as e:
        print(f'Procedure failed/n{e}')
