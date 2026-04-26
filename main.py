#pythonログ解析ツール

#4/26:ERROR抽出（表示）、count結果を記載した書き込みファイルを作成
count_ERROR=0
count_INFO=0
count_START=0

#書き込み用の変数はout
with open("output.txt","w",encoding="utf-8")as out:
    #読み込み用の変数はf
    with open("log.txt","r",encoding="utf-8")as f:

        #lineに改行含まれるからstrip()で改行消す
        for line in f:
            if "ERROR" in line:
                out.write(f"ERROR該当箇所：{line.strip()}\n")
                count_ERROR +=1

            if "INFO" in line:           
                out.write(f"INFO該当箇所：{line.strip()}\n")            
                count_INFO+=1


            if "START" in line:         
                out.write(f"START該当箇所：{line.strip()}\n")          
                count_START+=1

        out.write("------------\n")

        out.write(f"ERROR回数：{count_ERROR}\n")
        out.write(f"INFOの回数：{count_INFO}\n")
        out.write(f"STARTの回数：{count_START}\n")

        out.write("------------")
    

    
   
    