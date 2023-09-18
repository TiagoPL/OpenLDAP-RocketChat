def msg_chat(usuario, expiração):
    return f'''Olá {usuario}, sua senha no FreeIPA {expiração}.

Por favor, realize a troca da sua senha a partir deste website:

https://freeipa.domain.com.br/ipa/ui/

Caso a sua senha esteja expirada, não será possível a conexão com a VPN e os sistemas da 4linux ficarão indisponíveis.'''
