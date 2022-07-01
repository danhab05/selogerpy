import re
from flask import Flask,  request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
app = Flask(__name__)
CORS(app)


@app.route('/',  methods=["GET"])
def get_files():
    port = request.args.get('port')
    inst = request.args.get('inst')
    ip = request.args.get('ip')
    if ip is None:
        ip = "51.210.96.59"
    url = f'http://{ip}:{str(port)}/{inst}' + request.url.split('/')[3]
    print(url)
    d = os.popen(f'curl -sb -H "Accept: application/json" "{url}"').read()
    return str(d)


@app.route('/2',  methods=["GET"])
def get_moovie():
    title = request.args.get('title')
    url = f'http://37.187.53.89:8081?title=' + title.replace(" ", "%20")
    print(url)
    d = os.popen(f'curl -sb -H "Accept: application/json" "{url}"').read()
    return str(d)


if __name__ == "__main__":
    app.run(
    )
