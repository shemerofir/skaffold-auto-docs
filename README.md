 <p align="center">
 <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="dm2macoff" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://il.linkedin.com/in/dm2macoff?trk=profile-badge">Denis Marshall Tumakov</a></div>
              
 <h1 align="center">Skaffold Doco</h1>
 <p align="center">Denis Tu Feb, 2022</p>

 ![GitHub last commit](https://img.shields.io/github/last-commit/DmarshalTU/Skaffold-doco?style=plastic)

</p>

## 🔧 Technologies & Tools
![](https://img.shields.io/badge/OS-Linux-informational?style=flat&logo=linux&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-Kubernetes-informational?style=flat&logo=kubernetes&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-Ansible-informational?style=flat&logo=ansible&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-Terraform-informational?style=flat&logo=terraform&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-BotAPI-informational?style=flat&logo=telegram&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-Skaffold-informational?style=flat&logo=skaffold&logoColor=white&color=2bbc8a)

## &#x1f4c8; GitHub Stats

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=DmarshalTU&repo=Skaffold-Doco)](https://github.com/DmarshalTU/Skaffold-Doco)


## 📚 How to use Skaffold on remote clusster
### Developer station configuration
**IMPORTANT**: 
1. Make sure you have [Docker](https://www.docker.com/), [MiniKube](https://minikube.sigs.k8s.io/docs/start/), [Helm](https://helm.sh/) and [Ansible](https://docs.ansible.com/ansible/2.7/installation_guide/intro_installation.html) installed on your computer.
2. Install [Skaffold](https://skaffold.dev/).

* Configure the .kube/config to have both local and remote context
```yaml
ApiVersion: v1
clusters:
- cluster:
    certificate-authority-data: <Need to be copied from your remote cluster>
    server: https://<atlantic-master-node-ip>:6443
  name: cluster_name --> this is the name of my remote cluster
contexts:
- context:
    cluster: cluster_name --> this is the name of my remote cluster
    namespace: namespace -->default namespace on remote cluster
    user: default -->copied from remote cluster
  name: default  --> copied from remote cluster
current-context: default
kind: Config
preferences: {}
users:
- name: default --> user for remote cluster
  user:
    client-certificate-data: <Need to be copied from your remore cluster>
    client-key-data: <Need to be copied from your remore cluster>
  ```
  #TODO: add functoin to python script to copy the .kube/config file to the local machine

* Configure docker registry
```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

* Edit your /etc/hosts file and add the following line 
```bash
<Your VM IP> devrepo
```

* Add skaffold.yaml file to your project
```bash
touch skaffold.yaml
```

* Add skaffold.yaml file which contains info on the build and deploy steps of your microservice.

```yaml
#TODO add info on build and deploy steps
```
### Steps that need to be done **on each node** of your Remote Cluster
* Configure the cluster to work with our insecure registry
- Edit /etc/rancher/rke2/registries.yaml and add the following entry under mirrors key:
```yaml
devrepo:5000:
  endpoint:
    - "http://devrepo:5000"
```

* Restart the node:
```bash
sudo systemctl restart rke2-server # use this command for master node
sudo systemctl restart rke2-agent  # use this command ONLY for worker node!
#make sure the node is a worker node and not a master node using command "kubectl get nodes",
#otherwise, running the command on a master node will harm the installation.
#it's possible that all the nodes are masters.
```


### Skaffold commands:
```bash
skaffold dev #build and deploy your app every time your code changes
skaffold run #build and deploy your app once, similar to a CI/CD pipeline
skaffold run --tail	#same as before but will also tail the logs in your console
skaffold delete
```

# Automate the deployment process
```bash
git clone https://github.com/DmarshalTU/skaffold-doco.git
cd skaffold-doco
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python main.py
```