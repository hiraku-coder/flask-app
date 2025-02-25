from flask import Flask

app = Flask(__name__)
app.secret_key = "your_secret_key"  # セッションの暗号化キー


@app.route('/')
def home():
    return "Hello, Flask!"
