#pythonログ解析ツール

#4/25:ERROR抽出（表示）、countもする
count=0
with open("log.txt","r",encoding="utf-8")as f:

    for line in f:
        if "ERROR" in line:

            print(f"ERROR該当箇所：{line}")

            count +=1
            print(f"ERROR回数：{count}")

    