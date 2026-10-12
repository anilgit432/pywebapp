import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+ "! Welcome to m,y DevOps practice app."
    return 'i am learning jenkins CI/CD'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
