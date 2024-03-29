# Flask実装練習
***
## Overview  
Flaskの実装練習  
***  
## Note
***  
### ディレクトリの基本構造
```
(any directory)
 ├app/
 │　├templates/
 │　├static/
 │　└app.py
 └run.py
 ```

templates HTMLファイルを入れる場所  
static CSSやJS,画像ファイルを入れる場所  
app.py アプリロジックを書く ルーティングの話を書いたりする  
run.py Webサーバを立てるための実行ファイル  

動かし方  
`python run.py`

### Web画像表示
staticの下にimagesのdirをたす
```
(any directory)
 ├app/
 │　├templates/
 │　│　└index.html
 │　├static/
 │　│　└images/
 │　│　　└torii.jpg
 │　└app.py
 └run.py

 ```
### クエストリングをHTMLに反映  
render_template()の引数に値を入れることができるようにする  
app.pyの編集  
`http://127.0.0.1:5000/index?name=massaman`  
を`run.py`を実行した後にURL指定すると`?name=massaman` の`massaman`をtitleにnameという変数を入れている  

### if文制御  
htmlのレンダリングの際, if文によって表示するHTMLを変更する  
クエストリングによって表示するHTMLの内容を変更する処理を書く(このときHTMLないのカッコに注意...)  
templates/index.html を編集

### for文制御  
app.py の中で処理を行なった後,HTMLの中にレンダリングする処理の記述  
app.pyとindex.html を編集 (ここまで20191029)  
(ここから 20191030)  
for文の値をapp.pyの中で引き渡してHTMLの中にレンダリングすることは可能  

### POSTリクエストの処理  
ユーザーからポストされたデータを使用して動的なページを作成する  
index.htmlとapp.pyの編集  
基本的にはフォームと一緒に処理をする　テキストなど  

### SQLのセットアップ  
modelsのdirを直下にたす(SQLの制御)  
```
(any directory)
 ├app/
 │　├templates/
 │　│　└index.html
 │　├static/
 │　│　└images/
 │　│　　└torii.jpg
 │　└app.py
 ├models/(ここの中身を作る)
 │　├__init__.py(モジュールとして呼び出すためのfile)
 │　├models.py(カラム等の制御を行う際の.py file)
 │　└database.py(DBとの接続を管理する .py file)
 └run.py
 ```  
 主に `models.py` と `database.py` を作成していく  
 実行する際に`sqlalchemy` が必要なのでpipでDLする  
 database.py をpythonの対話シェルの状態でimportして,対話モードでdbにinsertする  
 `onegai.db`のあるdirで `sqlite3 onegai.db` をすることでSQLiteに入ることが可能  
 `Select * from onegaicontents;` のコマンドでDBの中にinsertされたデータの確認が可能

 ex)
 ```
 DBのイニシャライズ
 >>> from models.database import init_db  
 >>> init_db()  
 DBへのデータインサート
 >>> from models.database import db_session  
 >>> from models.models import OnegaiContent  
 >>> c1 = OnegaiContent("お願いします","5000兆円ください")  
 >>> c2 = OnegaiContent("助けてください","ぽんぽんぺいん")  
 >>> c3 = OnegaiContent("許してください","なんでもしますから")  
 >>> db_session.add(c1)  
 >>> db_session.add(c2)  
 >>> db_session.add(c3)  
 >>> db_session.commit()  
 ```  
 DBからHTMLに表示する  

### UIの実装(Databaseをweb上から処理する)  
レコードの追加・更新・消去の処理を追加    
index.html と app.pyの中を編集  
HTMLは表示の場所を変えるだけなのでそんなに難しいことはない  
<追加>  
```
@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    #対話型pythonでやった処理を実際に関数にしただけ
    return index()
```  
<編集>  
```
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
```  
<消去>  
```
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
```  
### ログイン&ユーザー管理  
ログイン機能,新規ユーザー登録, ログアウト機能　の実装  
新しいHTML, `top.html`と`newcomer.html`を作成  
`models.py` の中に `User`のクラスを追加する

## REFERENCE  
[参考資料](https://qiita.com/kiyokiyo_kzsby/items/0184973e9de0ea9011ed)

## Author
Masayoshi Tsuruoka  
[HP](https://www.ht.sfc.keio.ac.jp/~massaman/)  
[GIT](https://github.com/Masayo4)   
