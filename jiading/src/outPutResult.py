import pandas as pd
import os
def outPut(prediction,methodName,base="/home/jiading/Desktop/Don't overfit/Don-t_Overfit-PolyU/jiading/results"):
    index=250
    methodName=methodName+".csv"
    path=os.path.join(base,methodName)
    fout=open(path,'w')
    fout.write("id,target\n")
    for line in prediction:
        fout.write(str(index)+","+str(line)+"\n")
        index+=1
    fout.close()
