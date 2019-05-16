from flask import Flask
import os

app = Flask(__name__)


# voor als er geen pagina naam is opgegegeven
@app.route('/')
def root():
    data = open("home.html").read()
    return data


@app.route('/<path:filename>', methods=['GET'])
def pagina(filename):
    data = open(filename).read()
    return data


if __name__ == '_main_':
    app.run()
