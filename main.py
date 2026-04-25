#pythonログ解析ツール

#4/25:ファイル読み込み
#ファイルパス変えても読めるか
#相対パス
with open("log.txt","r",encoding="utf-8")as f:
    lines=f.read().splitlines()
    print(lines)

#絶対パスはスラッシュ使う
with open("C:/Users/Risaj/python_logkaisekitool/python_logkaisekitool/log.txt","r",encoding="utf-8")as f:
    lines=f.read().splitlines()
    print(lines)

print("変更テスト")

