import loadData as load
import outPutResult as out
from sklearn.linear_model import Lasso
from sklearn.feature_selection import RFECV
x_train,y_train,x_test=load.loadDataWithoutProbing()
lasso = Lasso(alpha=0.031, tol=0.01, random_state=213, selection='random')
selector=RFECV(estimator=lasso,step=1,min_features_to_select=15)
selector.fit(x_train,y_train)
prediction=selector.predict(x_test)
out.outPut(prediction,"lasso(only RFECV)-15features")