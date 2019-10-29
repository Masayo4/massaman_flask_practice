#ルーティングのためのファイル
from flask import Flask,render_template
#モジュールインポート

app = Flask(__name__)
#Flaskのオブジェクト生成

#/へのアクセスの処理
@app.route("/")
def hello():
    return "Hello World"

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
