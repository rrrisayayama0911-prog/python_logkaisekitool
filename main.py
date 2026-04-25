#pythonログ解析ツール

#4/26:ERROR抽出（表示）、countもする
count_ERROR=0
count_INFO=0
count_START=0

with open("log.txt","r",encoding="utf-8")as f:

    #lineに改行含まれるからstrip()で改行消す
    for line in f:
        if "ERROR" in line:
            print(f"ERROR該当箇所：{line.strip()}")
            count_ERROR +=1
        
        if "INFO" in line:           
            print(f"INFO該当箇所：{line.strip()}")            
            count_INFO+=1
            
            
        if "START" in line:         
            print(f"START該当箇所：{line.strip()}")          
            count_START+=1
            
    print("------------")
            
    print(f"ERROR回数：{count_ERROR}")
    print(f"INFOの回数：{count_INFO}")
    print(f"STARTの回数：{count_START}")
    
    print("------------")

    