from threading import Thread
from free_ipa import ldap
from msg import msg_chat
from flask import Flask
from time import sleep
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return "Password check lives!"

@app.route("/chat")
def send_return():
    
    usuarios_a_vencer = ldap()
    usuarios_a_vencer_string = ''
    for name in usuarios_a_vencer:
        usuarios_a_vencer_string += f'{name} <br /> '

    # Retorna uma mensagem ao request e finaliza a conexão, enquanto a API continua a executar:
    Thread(target = send_chat).start()
    return (f'Os seguintes usuarios estão vencidos ou a vencer e serão notificados pelo chat: <br /> {usuarios_a_vencer_string}')

def send_chat():
    
    usuarios_a_vencer = ldap()

    # Envia uma mensagem no rocketchat pra cada usuario vencido/a vencer:
    for usuario, expiração in usuarios_a_vencer.items():

        headers = {}
        json_data = {
            'channel': f'@{usuario}',
            'username': '4SecBot',
            'avatar': 'https://blog.domain.com.br/wp-content/uploads/2022/10/4secbot.png',
            'text': msg_chat(usuario, expiração)
                    }
        
        requests.post('https://chat.4linux.com.br/hooks/123/123', headers=headers, json=json_dat, verify=False)
        print(f'Enviando mensagem para: {usuario}')
        sleep(7)

if __name__ == '__main__':
    app.run(debug=True)
