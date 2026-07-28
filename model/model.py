from sklearn.decomposition import PCA
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

class Genes:
    def __init__(self,param,n):
        self.pca=PCA(n)
        self.grid=GridSearchCV(KernelDensity(kernel="gaussian"), param,cv=5,n_jobs=-1)
    def fit(self,X):
        T=self.pca.fit_transform(X)
        self.grid.fit(T)
        self.kde=self.grid.best_estimator_
    def sample(self,n):
        S=self.kde.sample(n)
        return self.pca.inverse_transform(S)
    def fil(self,X):
        return np.where(X > X.mean(axis=1, keepdims=True), X, 0)
    def fil_sample(self,n):
        S=self.kde.sample(n)
        S=self.pca.inverse_transform(S)
        return self.fil(S)


class Digiter:
    def __init__(self,gs):
        self.gs=gs
    def gen(self,xs:str):
        xs=str(xs)
        ps=[]
        for i in xs:
            if i.isdigit():
                ps.append(self.gs[int(i)].fil_sample(1).reshape(28,28))
        imag=np.concatenate(ps,axis=1)
        return imag
    def cut(self, imag):
        return np.delete(imag,np.where(imag.mean(axis=0)==0),axis=1)
    def gen_cut(self,xs):
        imag=self.gen(xs)
        return self.cut(imag)
    def get_param(self):
        parm={}
        for i,e in enumerate(self.gs):
            kde=e.kde.get_params()
            pca=e.pca.get_params()
            parm[i]=(kde,pca)
        return parm
