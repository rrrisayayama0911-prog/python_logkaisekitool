#pythonログ解析ツール

#4/25:1行ずつ読み込み
#.strip()の意味理解（改行除去）
#for line in fがなぜ1行ずつなのか説明できるか

"""
#.strip()の意味理解（改行除去）
sprip():デフォルトでは両端の連続する空白文字が取り除かれる。
strip('指定文字'):split("\n") → 「\nだけ」で区切る
splitlines():行ごとに分割する
"""

"""
#Windowsの改行は\r\nより、split()だと\rだけ残す
\rと\nを組み合わせて、行の終わりと次の行への移動になるので配列(list)にならない
print(type(変数))で<class 'list'>かどうかわかる


#for line in fがなぜ1行ずつなのか説明できるか
ファイルオブジェクトはイテレータ(次の要素を返す)として動作し、
for文で回すと1回ごとに次の要素を返します。

その要素が「1行」になるように、
内部では改行コード（\n）を区切りとして読み込む実装になっているため、
結果として1行ずつ処理できるようになっています。
"""

#相対パスsprip()
with open("log.txt","r",encoding="utf-8")as f:
    lines=f.read() #read()は全体
    print(lines.strip())

#相対パスsplitlines()
with open("log.txt","r",encoding="utf-8")as f:
    lines=f.read().splitlines()#read()は全体
    print(lines)

#絶対パスはスラッシュ使う
with open("C:/Users/Risaj/python_logkaisekitool/python_logkaisekitool/log.txt","r",encoding="utf-8")as f:
    lines=f.read().splitlines()
    print(lines)

#raw文字(ファイルパスの前にr:と付け加える)でバックスラッシュ使う。エスケープシーケンスを無視させて単純な文字列として認識させる

with open(r"C:\Users\Risaj\python_logkaisekitool\python_logkaisekitool/log.txt","r",encoding="utf-8")as f:
    lines=f.read().splitlines()
    print(lines)
