'''
from app.app import app

if __name__ == "__main__":
    app.run()
'''
from app import app  # ✅ app.py から Flask インスタンスをインポート

if __name__ == "__main__":
    app.run()  # ✅ Render/Gunicorn を使う場合は、これは実行されない
