#ルーティングのためのファイル
from flask import Flask,render_template,request
#モジュールインポート
from models.models import OnegaiContent
#modelsの中で作成したクラスを呼び出す

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
    #okyo = ["色不異空","空不異色","色即是空","空即是色"]
    #ステップ2で作成 for制御
    #return render_template("index.html",name=name,okyo=okyo)
    #ここまでステップ2
    #以下DBからデータを引き出す際のコード
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html",name=name,all_onegai=all_onegai)


#postをする処理を追記
@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    #okyo = ["色不異空","空不異色","色即是空","空即是色"]
    #return render_template("index.html",name=name,okyo=okyo)
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html",name=name,all_onegai=all_onegai)


if __name__ == '__main__':
    app.run(debug=True)
