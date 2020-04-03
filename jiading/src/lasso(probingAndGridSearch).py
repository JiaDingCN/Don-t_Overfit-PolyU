import loadData as load
import numpy as np
import outPutResult as out
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
x_train,y_train,x_test=load.loadData()
parameters={'alpha':list(np.arange(0.005,1,0.005))}
lasso = Lasso(tol=0.01, random_state=213, selection='random')
clf=GridSearchCV(lasso,parameters)
clf.fit(x_train,y_train)
prediction=clf.predict(x_test)
out.outPut(prediction,"lasso(probing and gridSearch)")



