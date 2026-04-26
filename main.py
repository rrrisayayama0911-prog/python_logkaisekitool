#pythonログ解析ツール

#gui切り替え

#関数で処理をまとめる、3つの受け取る箱(変数)を用意
def analyze_log(in_f,out_f,keywords): #keywordはcui時点では使用しない
    
    count_ERROR=0
    count_INFO=0
    count_START=0


    #書き込み用の変数はout_f
    with open("output.txt","w",encoding="utf-8")as out_f:
        #読み込み用の変数はin_f
        with open("log.txt","r",encoding="utf-8")as in_f:

            #lineに改行含まれるからstrip()で改行消す
            for line in in_f:
                if "ERROR" in line:
                    #書き込みファイルの()の内容を文字列として書き込む
                    out_f.write(f"ERROR該当箇所：{line.strip()}\n")
                    count_ERROR +=1

                if "INFO" in line:
                    #書き込みファイルの()の内容を文字列として書き込む           
                    out_f.write(f"INFO該当箇所：{line.strip()}\n")            
                    count_INFO+=1


                if "START" in line:
                    #書き込みファイルの()の内容を文字列として書き込む         
                    out_f.write(f"START該当箇所：{line.strip()}\n")          
                    count_START+=1

            out_f.write("------------\n")

            out_f.write(f"ERROR回数：{count_ERROR}\n")
            out_f.write(f"INFOの回数：{count_INFO}\n")
            out_f.write(f"STARTの回数：{count_START}\n")

            out_f.write("------------")


#1回だけ呼ぶ、3つのデータを入れる
keywords =["ERROR","INFO","START"]
analyze_log("log.txt","output.txt",keywords)
    
    

    
   
    