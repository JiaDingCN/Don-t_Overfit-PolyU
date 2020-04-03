import loadData as load
import outPutResult as out
from sklearn.linear_model import Lasso
from sklearn.decomposition import PCA
pca=PCA(n_components=15)
x_train,y_train,x_test=load.loadData()
pca.fit(x_train)
x_train=pca.transform(x_train)
x_test=pca.transform(x_test)
lasso = Lasso(alpha=0.031, tol=0.01, random_state=213, selection='random')
lasso.fit(x_train,y_train)
prediction=lasso.predict(x_test)
out.outPut(prediction,"lasso(probing and PCA)15featuresChanged")