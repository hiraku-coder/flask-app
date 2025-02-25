'''
from app.app import app

if __name__ == "__main__":
    app.run()
'''
from app import app  # __init__.py 内の `app` を読み込む

if __name__ == "__main__":
    app.run()
