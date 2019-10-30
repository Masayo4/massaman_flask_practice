#ルーティングのためのファイル
from flask import Flask,render_template,request
#モジュールインポート
from models.models import OnegaiContent,User
#modelsの中で作成したクラスを呼び出す
from models.database import db_session
from datetime import datetime

from flask import session,redirect,url_for
from app import key
from hashlib import sha256
#追加import セッションや,リダイレクト, バスワード, ハッシュ化などのimportを行う

app = Flask(__name__)
#Flaskのオブジェクト生成
app.secret_key = key.SECRET_KEY
#なりすましがないように keyの解読を難しくする


#/へのアクセスの処理
@app.route("/")
#def hello():
#    return "Hello World"


@app.route("/index")
def index():
    #ステップ2で作成 クエストリング
    #name = request.args.get("name")
    #okyo = ["色不異空","空不異色","色即是空","空即是色"]
    #ステップ2で作成 for制御
    #return render_template("index.html",name=name,okyo=okyo)
    #ここまでステップ2
    #以下DBからデータを引き出す際のコード
    #all_onegai = OnegaiContent.query.all()
    #return render_template("index.html",name=name,all_onegai=all_onegai)
    #以下最終形態のルーティング
    if "user_name" in session:
        name = session["user_name"]
        all_onegai = OnegaiContent.query.all()
        return render_template("index.html",name=name,all_onegai=all_onegai)
    else:
        return redirect(url_for("top",status="logout"))

#postをする処理を追記 最終的に排除
#@app.route("/index",methods=["post"])
#def post():
    #name = request.form["name"]
    #okyo = ["色不異空","空不異色","色即是空","空即是色"]
    #return render_template("index.html",name=name,okyo=okyo)
    #all_onegai = OnegaiContent.query.all()
    #return render_template("index.html",name=name,all_onegai=all_onegai)

#HTMLからDBにデータを送るための関数
@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    #対話型pythonでやった処理を実際に関数にしただけ
    return redirect(url_for("index"))

@app.route("/update",methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    #現在のDBの中にあるものを特定して持ってくる
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    #最後にDBの更新
    #仕様的に重複するものだとエラーがでるので注意...(ここは本番の作るときは調べながら...)
    return redirect(url_for("index"))

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    #一致するものを消去するから全体をまず取り出す
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
        #DBの中にあるコンテンツを消去する
    db_session.commit()
    return redirect(url_for("index"))

#ログイン処理
@app.route("/login",methods=["post"])
def login():
    user_name = request.form["user_name"]#user名をフォームから取得
    user = User.query.filter_by(user_name=user_name).first() #名前が一致するものを探してくる
    if user:
        password = request.form["password"] #パスワードと認証しに行く
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest() #パスワードをハッシュ化する
        if user.hashed_password == hashed_password:
            session["user_name"] = user_name
            return redirect(url_for("index"))
            #両方一致したものはusernameと共にindexにリダイレクトする
        else:
            return redirect(url_for("top",status="wrong_password"))
            #passwordが間違っていると通知する
    else:
        return redirect(url_for("top",status="user_notfound"))
        #ユーザー名がなかった場合, ユーザーが存在しないことを通知する

#新規ユーザーの登録
@app.route("/registar",methods=["post"])
def registar():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer",status="exist_user"))
        #既存ユーザーがいるときはエラーを吐かせる
    else:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))

@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html",status=status)


@app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html",status=status)


if __name__ == '__main__':
    app.run(debug=True)
