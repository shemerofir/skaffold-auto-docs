import sh


def get_helm():
    print('Installin Helm')
    sh.sudo.bash(sh.curl('https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3'))
