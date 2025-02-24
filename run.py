
#"Hello World!"と表示されるWebアプリケーション
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello():
#    return 'python hello world!!!!!!'

#if __name__ == '__main__':
#    app.run(port=8000, debug=True)
from app.app import app  # app.py の `app` を明示的に指定

if __name__ == "__main__":
    app.run(debug=True)
