#ルーティングのためのファイル
from flask import Flask,render_template,request
#モジュールインポート
from models.models import OnegaiContent
#modelsの中で作成したクラスを呼び出す
from models.database import db_session
from datetime import datetime

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

#HTMLからDBにデータを送るための関数
@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    #対話型pythonでやった処理を実際に関数にしただけ
    return index()

@app.route("/update",methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    #現在のDBの中にあるものを特定して持ってくる
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    #最後にDBの更新
    #仕様的に重複するものだとエラーがでるので注意...(ここは本番の作るときは調べながら...)
    return index()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    #一致するものを消去するから全体をまず取り出す
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
        #DBの中にあるコンテンツを消去する
    db_session.commit()
    return index()


if __name__ == '__main__':
    app.run(debug=True)
