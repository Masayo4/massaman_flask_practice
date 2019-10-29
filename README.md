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




## REFERENCE  
[参考資料](https://qiita.com/kiyokiyo_kzsby/items/0184973e9de0ea9011ed)

## Author
Masayoshi Tsuruoka  
[HP](https://www.ht.sfc.keio.ac.jp/~massaman/)  
[GIT](https://github.com/Masayo4)   
