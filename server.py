from flask import Flask
from flask import request

from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])



def index():
    if request.method=="POST":
        content = request.json
        ##print(data['repository']['clone_url'])
        ##event=request.headers['X-GitHub-Event']
        return content['repository']['clone_url']
    elif request.method=="GET":
        return "GET Method"

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()