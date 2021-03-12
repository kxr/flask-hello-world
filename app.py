from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return a hello string."""
    return '<h1>Hello World :)</h1>'

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=False)
