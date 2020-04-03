import loadData as load
import outPutResult as out
from sklearn.linear_model import Lasso
from sklearn.feature_selection import RFE
x_train,y_train,x_test=load.loadData()
lasso = Lasso(alpha=0.031, tol=0.01, random_state=213, selection='random')
selector=RFE(lasso,15,1,0)
print("x_train's length is:",len(x_train[0]))
selector.fit(x_train,y_train)
print("after RFE,x_train's length is:",len(x_train[0]))
print("N_features %s" % selector.n_features_)
print("Support is %s" % selector.support_)
print("Ranking %s" % selector.ranking_)
prediction=selector.predict(x_test)
out.outPut(prediction,"lasso(RFE-test)-15features")