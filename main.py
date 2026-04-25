#pythonログ解析ツール

#4/25:ERROR抽出（表示）、countもする
count_ERROR=0
count_INFO=0
count_START=0

with open("log.txt","r",encoding="utf-8")as f:

    for line in f:
        if "ERROR" in line:

            print(f"ERROR該当箇所：{line}")
            count_ERROR +=1
            print(f"ERROR回数：{count_ERROR}\n")
        
        if "INFO" in line:
            
            print(f"INFO該当箇所：{line}")            
            count_INFO+=1
            print(f"INFOの回数：{count_INFO}\n")
            
        if "START" in line:
            
            print(f"START該当箇所：{line}")          
            count_START+=1
            print(f"STARTの回数：{count_START}\n")

    