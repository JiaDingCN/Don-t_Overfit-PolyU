import os
import readData as read
def loadData():
    prob=['0','9','15','16','17','24','33','39','43','45','63','65','73','80','89','90','91','98','101',
     '105','117','133','134','143','150','156','164','176','183','189','194','199','209','214','215',
     '217','221','227','228','230','237','239','240','244','253','258','276','295','298']
    prob_int=[]
    prob_int_test=[]
    for item in prob:
        prob_int.append(int(item)+2)
        prob_int_test.append(int(item)+1)
    data_dir= "/home/jiading/Desktop/Don't overfit/Don-t_Overfit-PolyU/data"
    filenameTrain=os.path.join(data_dir,'train.csv')
    filenameTest=os.path.join(data_dir,'test.csv')
    x_train,y_train=read.readCSVMatrixWithSelectionAndBeginningAndDividedAsNumber(filenameTrain,prob_int,1,1)
    x_test=read.readCSVMatrixWithSelectionAndBeginningAsNumber(filenameTest,prob_int_test,1)
    return x_train,y_train,x_test
def loadDataWithoutProbing():
    data_dir= "/home/jiading/Desktop/Don't overfit/Don-t_Overfit-PolyU/data"
    filenameTrain=os.path.join(data_dir,'train.csv')
    filenameTest=os.path.join(data_dir,'test.csv')
    x_train,y_train=read.readCSVMatrixAndBeginningBothAndDividedAsNumber(filenameTrain,1,2,1)
    x_test=read.readCSVMatrixAndBeginningBothAsNumber(filenameTest,1,1)
    return x_train,y_train,x_test

