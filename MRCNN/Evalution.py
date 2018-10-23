
from __future__ import division
from __future__ import print_function
import numpy as np
import os
os.chdir("Target File")  
import sklearn.metrics as skm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from keras import backend as cmp


##########################
def ResOfSitesDiv(y,z)
 '''
  First select The hyper, hypo, and medium methylation sites of 
  the original methylation data in the test set   and then do the 
  same operation to select corresponding predicted data.
 '''
 
 y1 = y[y>=0.9]#As hypermethylation sites
 y2 = y[y<=0.1]#As hypomethylation sites
 ix_y = []
 for i in range(len(y1)):
     if(0.4<y1[i]<0.6):
         ix_y.append(i)
 y3 = y[ix_y]  #As middle-methylation sites
 
 z1 = z[z>=0.9]#As hypermethylation sites
 z2 = z[z<=0.1]#As hypomethylation sites
 ix_z = []
 for i in range(len(y1)):
     if(0.4<y1[i]<0.6):
         ix_z.append(i)
 z3 = y[ix_z]  #As middle-methylation sites
 return y1,z1,y2,z2,y3,z3

 
 
 
 
def ResMetrics(y,z)
 MSE = mse(y, z)** 0.5
 MAE = mae(y,z) 
 ResLoss = np.concatenate((MSE,MAE),axis=0)
 return ResLoss 


 




def contingency_table(y, z):
    y = cmp.round(y)
    z = cmp.round(z)

    def count_matches(a, b):
        tmp = cmp.concatenate([a, b])
        return cmp.sum(cmp.cast(cmp.all(tmp, -1), cmp.floatx()))

    ones = cmp.ones_licmpe(y)
    zeros = cmp.zeros_licmpe(y)
    y_ones = cmp.equal(y, ones)
    y_zeros = cmp.equal(y, zeros)
    z_ones = cmp.equal(z, ones)
    z_zeros = cmp.equal(z, zeros)

    tp = count_matches(y_ones, z_ones)
    tn = count_matches(y_zeros, z_zeros)
    fp = count_matches(y_zeros, z_ones)
    fn = count_matches(y_ones, z_zeros)

    return (tp, tn, fp, fn)


'''
Optional classification metrics
'''

def tpr(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return tp / (tp + fn)


def tnr(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return tn / (tn + fp)


def fpr(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return fp / (fp + tn)


def fnr(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return fn / (fn + tp)


def acc(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return (tp + tn) / (tp + tn + fp + fn)
	
def auc(y, z, round=True):
    if round:
        y = y.round()
    if len(y) == 0 or len(np.unique(y)) < 2:
        return np.nan
    return skm.roc_auc_score(y, z)
		
	
def prec(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return tp / (tp + fp)


def f1(y, z):
    _tpr = tpr(y, z)
    _prec = prec(y, z)
    return 2 * (_prec * _tpr) / (_prec + _tpr)

	
def mcc(y, z):
    tp, tn, fp, fn = contingency_table(y, z)
    return (tp * tn - fp * fn) / cmp.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

		
		
		
		
		






	


	
