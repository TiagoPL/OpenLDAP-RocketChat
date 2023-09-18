from python_freeipa import ClientMeta
from datetime import date


FREEIPA_HOST = '123'
FREEIPA_USERNAME = '123'
FREEIPA_PASSWORD_KEY = "123"


def ldap():
    # Faz o acesso ao LDAP e cria uma lista com todos os usuarios:
    client = ClientMeta(FREEIPA_HOST)
    client.login(FREEIPA_USERNAME, FREEIPA_PASSWORD_KEY)
    lista = client.user_find()

    numero_de_usuarios = len(lista['result'])
    usuarios_a_vencer = {}

    # Verifica o user e a expiração de todos os usuarios:
    for user in range(0, numero_de_usuarios):
        username = lista['result'][user]['uid'][0]
        expiration = lista['result'][user]['krbpasswordexpiration'][0]['__datetime__'][:8]

        expiration_date = date(int(expiration[:4]), int(expiration[4:6]), int(expiration[6:]))
        today = date.today()

        # Verifica se o usuario não é de serviço:
        usuarios_de_serviço = ['svc', 'mautic', 'jenkins', 'alert', 'wekan', 'domain', 'lgpd', 'revisores']
        usuario_de_serviço_check = False

        for user in usuarios_de_serviço:
            if user in username:
                usuario_de_serviço_check = True
        
        # Adiciona o usuario ao dicionario se estiver pra vencer ou vencido:
        if usuario_de_serviço_check == False:
            if expiration_date < today:
                estado = 'está expirada!'
                usuarios_a_vencer[str(username)] = str(estado)

            elif abs(today - expiration_date).days <= 15:
                estado = f'expira em {abs(today - expiration_date).days} dias!'
                usuarios_a_vencer[str(username)] = str(estado)

    return usuarios_a_vencer
