from get_config import get_config
from get_ansible import get_ansible
from get_helm import get_helm
from get_skaffold import get_skaffold
from get_docker import get_docker
from get_minikube import get_minikube
from get_regs import get_registries
from edit_hosts import edit_hosts
from c_registry import c_registry


if __name__ == '__main__':
    edit_hosts()
    get_docker() #
    c_registry() #
    get_ansible() # 
    #get_helm() # 
    get_minikube() # 
    get_skaffold() # 
    get_config()
    get_registries()
    edit_hosts()
