import os
import pandas as pd
data_dir= "/home/jiading/Desktop/Don't overfit/Don-t_Overfit-PolyU/data"
filenameTrain=os.path.join(data_dir,'train.csv')
filenameTest=os.path.join(data_dir,'test.csv')
train=pd.read_csv(filenameTrain,index_col=0) #去掉第一行的預設值
x_train=train.iloc[:,1:]#每一行,列(除了target)
y_train=train['target']
x_test=pd.read_csv(filenameTest,index_col=0) #去掉第一行的預設值
prob=['0','9','15','16','17','24','33','39','43','45','63','65','73','80','89','90','91','98','101',
 '105','117','133','134','143','150','156','164','176','183','189','194','199','209','214','215',
 '217','221','227','228','230','237','239','240','244','253','258','276','295','298']
prob_int=[]
for item in prob:
    prob_int.append(int(item))
print(x_train)
x_train_selected=[]
x_test_selected=[]

