import qrcode
import os

# FlaskアプリのURL（ローカルIP & ポート8000を明示）
BASE_URL = "http://192.168.10.126:8000"  # ← ここにポート8000を指定

# QRコードでアクセスするURL（トークンなし）
url = f"{BASE_URL}/"

# トークンを付ける場合（必要なら）
# token = "abcdef"
# url = f"{BASE_URL}/?token={token}"

# 保存先パス（staticフォルダ内に保存）
save_path = os.path.join(os.path.dirname(__file__), "static", "qrcode.png")

# QRコードを生成
img = qrcode.make(url)

# 画像を保存
img.save(save_path)

print(f"✅ QRコードを作成しました: {save_path}")
print(f"🔗 QRコードのURL: {url}")
