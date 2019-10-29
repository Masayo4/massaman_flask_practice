#ルーティングのためのファイル
from flask import Flask,render_template,request
#モジュールインポート

app = Flask(__name__)
#Flaskのオブジェクト生成

#/へのアクセスの処理
@app.route("/")
#def hello():
#    return "Hello World"

@app.route("/index")
def index():
    #ステップ2で作成 クエストリング
    name = request.args.get("name")
    return render_template("index.html",name=name)
    #ここまでステップ2

if __name__ == '__main__':
    app.run(debug=True)
