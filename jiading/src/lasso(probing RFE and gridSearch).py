import loadData as load
import outPutResult as out
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.feature_selection import RFE
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
'''
No,it doesn't work.
You can't both use RFE and GridSearch
x_train,y_train,x_test=load.loadData()
estimator=[('lasso',Lasso(tol=0.01, random_state=213, selection='random')),('RFE',RFE(estimator='lasso',step=1,n_features_to_select=15))]
pipe=Pipeline(estimator)
parameters={'lasso__alpha':list(np.arange(0.005,1,0.005))}
clf=GridSearchCV(pipe,parameters)
clf.fit(x_train,y_train)
prediction=clf.predict(x_test)
out.outPut(prediction,"lasso(RFE)-15features")
'''