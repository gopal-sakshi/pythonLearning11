from flask import Flask
from football23.clubs23 import clubs23_bp
app = Flask(__name__)

app.register_blueprint(clubs23_bp)

#####################################################################
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/greetInSpanish')
def hola():
    return 'HalaMadrid!!'
#####################################################################
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8010)