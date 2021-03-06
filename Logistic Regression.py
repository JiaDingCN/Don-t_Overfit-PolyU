import os
import pandas as pd

data_dir= 'C:/Users/user/Desktop/class/maching learning/project/group/Don-t_Overfit_PolyU/dataset'

# features selected by RFECV with lasso
features = ['16', '33', '43', '45', '52', '63', '65', '73', '90', '91', '117', '133',
            '134', '149', '189', '199', '217', '237', '258', '295']

#observe train data
filenameTrain=os.path.join(data_dir,'train.csv')
train=pd.read_csv(filenameTrain)

#observe test data
filenameTest=os.path.join(data_dir,'test.csv')
test=pd.read_csv(filenameTest)

#load prepared data
def get_train_data():
    train=pd.read_csv(filenameTrain,index_col=0) #去掉第一行的預設值
    x_train=train.iloc[:,1:]#每一行,列(除了target)
    y_train=train['target']
    return x_train,y_train

def get_test_data():
    test=pd.read_csv(filenameTest,index_col=0) #去掉第一行的預設值
    #test=test[features]
    return test
    
    
x_train0,y_train=get_train_data()
test=get_test_data()


#使用Logistic Regression之前需要先對資料做特徵縮放
#使用sklearn.preprocessing.StandardScaler類，使用該類的好處在於可以保存訓練集中的參數（均值、方差）直接使用其對象轉換測試集數據。
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=pd.DataFrame(scaler.fit_transform(x_train0),columns=x_train0.columns,index=x_train0.index)
test=pd.DataFrame(scaler.fit_transform(test),columns=test.columns,index=test.index)

#logistic regression
from sklearn.linear_model import LogisticRegression
log = LogisticRegression(
        penalty='l1', #l1:拉普拉斯分佈; l2:高斯分佈
        dual=False,
        tol=1e-4,
        C=0.2, #越小的數值表示越強的正則化，正則化是用來防止模型過擬合的過程 1.0/0.5/0.3/0.2/0.1
        fit_intercept=False, #指定是否應該向決策函數添加常量(即偏差或截距)
        intercept_scaling=1, #：僅在solver為”liblinear”，且fit_intercept設置為True時有用
        class_weight='balanced',#{0:0.4,1:0.6}, #比如對於0,1的二元模型，我們可以定義class_weight={0:0.9,1:0.1}，這樣類型0的權重為90%，而類型1的權重為10%:None/{0:0.9,1:0.1}/balanced
        random_state=None,
        solver='liblinear', #liblinear適用於小數據集，而sag和saga適用於大數據集因為速度更快:liblinear/saga/newton-cg/lbfgs/sag
        max_iter=100,#僅在正則化優化算法為newton-cg, sag和lbfgs才有用，算法收斂的最大迭代次數。
        multi_class= 'ovr', #ovr/multinomial:多分類
        verbose=0, #印出模型
        warm_start=False, #如果為True，則下一次訓練是以追加樹的形式進行（重新使用上一次的調用作為初始化）
        n_jobs=1 #1的時候，用CPU的一個內核運行程序，2的時候，用CPU的2個內核運行程序。為-1的時候，用所有CPU的內核運行程序
        )


log.fit(x_train,y_train)


#result
prediction = log.predict(test)
prediction = pd.DataFrame(prediction)
prediction.index += 250
prediction.columns = ['target']
prediction.to_csv('C:/Users/user/Desktop/class/maching learning/project/group/Don-t_Overfit_PolyU/result/Logistic Regression(feature_select).csv', index_label='id', index=True)
