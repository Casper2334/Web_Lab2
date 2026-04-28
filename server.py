import ssl
from flask import Flask

app = Flask(__name__)

# Эндпоінт
@app.route('/hello',  methods=['GET'])
def hello():

    return "Hello from Туровський Максим KP-31"

if __name__ == '__main__':
    # SSL контекст
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    # Обмеження версії до TLS v1.2
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2

    # Це критично важливо, щоб Wireshark міг розшифрувати трафік маючи лише приватний ключ.
    context.set_ciphers('AES128-GCM-SHA256')


    # Сертифікат та ключ
    context.load_cert_chain(
        certfile='localhost+1.pem',
        keyfile='localhost+1-key.pem'
    )

    # Запуск
    app.run(host='127.0.0.1', port=5443, ssl_context=context)