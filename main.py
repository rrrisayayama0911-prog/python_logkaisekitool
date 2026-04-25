#pythonログ解析ツール

#4/25:ERROR抽出（表示）

count=0

with open("log.txt","r",encoding="utf-8")as f:
    
    for line in f:

        if "ERROR" in line:
            print(line)

            count +=1
print(count)