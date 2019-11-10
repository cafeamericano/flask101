import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello World</h1><p>Sent to you by a server running Flask.</p>"

@app.route('/json', methods=['GET'])
def makeJSON():
    return flask.jsonify(name='Matthew', favoriteColor='Orage')

@app.route('/htmlfile', methods=['GET'])
def sendHTMLFile():
    return flask.current_app.send_static_file('index.html')

@app.route('/pngfile', methods=['GET'])
def sendPNGFile():
    return flask.current_app.send_static_file('catnose.png')

app.run(port=9000)