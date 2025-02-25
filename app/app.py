'''
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # セッションの暗号化キー

# ユーザー情報
users = {
    "hiraku": "1836"
}

@app.route("/")
def home():
    """ホーム画面（Hello World!）"""
    return render_template("home.html")  # ホーム画面（Hello World!）

@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    """ログインページ（未認証時） / マイページ（認証後）"""
    if "username" not in session:
        return redirect(url_for("login"))  # 🔹 ログインしていなければログインページへ

    return render_template("mypage.html", username=session["username"])  # ✅ 正しくマイページを表示

@app.route("/login", methods=["GET", "POST"])
def login():
    """ログインページ"""
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # 認証チェック
        if username in users and users[username] == password:
            session["username"] = username  # ✅ セッションにユーザー名を保存
            return redirect(url_for("mypage"))  # ✅ ログイン成功 → マイページへリダイレクト
        else:
            error = "ユーザー名またはパスワードが間違っています。"

    return render_template("login.html", error=error, username=request.form.get("username", ""))

@app.route("/logout")
def logout():
    """ログアウト処理"""
    session.pop("username", None)  # セッションから削除
    return redirect(url_for("home"))  # ✅ ホームへリダイレクト

if __name__ == "__main__":
    app.run(debug=True)
'''
from flask import Flask, render_template, request, redirect, url_for, session

#app = Flask(__name__)
#app.secret_key = "your_secret_key"  # セッションの暗号化キー

# 仮のQRコード用トークン（本番ではDBで管理するのが望ましい）
valid_tokens = {"abcdef": True}  # token のリスト（認証情報は保存しない）

@app.route("/")
def home():
    """ホームページ（QRコードからのアクセスも含む）"""
    token = request.args.get("token")
    
    if token and token in valid_tokens:
        return render_template("home.html", qr_access=True)  # QRコード経由のアクセスを識別

    return render_template("home.html", qr_access=False)

@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    """ログインページ（未認証時） / マイページ（認証後）"""
    if "username" not in session:
        return redirect(url_for("login"))  # 🔹 ログインしていなければログインページへ

    return render_template("mypage.html", username=session["username"])  # ✅ 正しくマイページを表示

@app.route("/login", methods=["GET", "POST"])
def login():
    """ログインページ"""
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # 認証チェック
        if username == "hiraku" and password == "1836":
            session["username"] = username  # ✅ セッションにユーザー名を保存
            return redirect(url_for("mypage"))  # ✅ ログイン成功 → マイページへリダイレクト
        else:
            error = "ユーザー名またはパスワードが間違っています。"

    return render_template("login.html", error=error, username=request.form.get("username", ""))

@app.route("/logout")
def logout():
    """ログアウト処理"""
    session.pop("username", None)  # セッションから削除
    return redirect(url_for("home"))  # ✅ ホームへリダイレクト
'''
if __name__ == "__main__":
    app.run(debug=True)
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)  # ✅ これで外部アクセスが可能！
