import loadData as load
import outPutResult as out
from sklearn.linear_model import Lasso
from sklearn.feature_selection import RFE
x_train,y_train,x_test=load.loadDataWithoutProbing()
lasso = Lasso(alpha=0.031, tol=0.01, random_state=213, selection='random')
selector=RFE(lasso,15,1,0)
selector.fit(x_train,y_train)
prediction=selector.predict(x_test)
out.outPut(prediction,"lasso(only RFE)-15features")