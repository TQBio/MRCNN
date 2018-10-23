from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE





def ErrDisstribution(y,z):
 Err = y - z
 sns.distplot(Err,rug=True, hist=False)
 
 return "Disstribution of Error Plot is as follow:"




 
def Boxplot(x,y,z):
 fig= plt.subplots(figsize=(10,6))
 plt.subplot(111)
 h = pd.Series(x)
 l = pd.Series(y)
 m = pd.Series(z)
 data = pd.DataFrame({"hyper": h, "hypo": l, "mid": m})
 data.boxplot(patch_artist=True, 
             showmeans=True, 
             widths=0.2,
             boxprops = {'color':'red','facecolor':'black'}, 
             flierprops = {'marker':'o','markerfacecolor':'lightcyan','color':'lightgray'}, 
             meanprops = {'marker':'D','markerfacecolor':'y'}, 
             medianprops = {'linestyle':'--','color':'orange'}) 
 plt.ylim(-0.6,0.6)
 
 return "The barplot of regression is as follow:"


 
 
def BarComplot(d1,d2,d3,p1,p2,p3):
 pos = list(range(len(d1)))
 width = 0.2
 fig= plt.subplots(figsize=(12,11))
 ax1 = plt.subplot(211)
 plt.bar(pos,d1,width,alpha=0.5,color='b')
 plt.bar([p + width for p in pos],d2,width,alpha=0.5,color='y')
 plt.bar([p + width*2 for p in pos],d3,width,alpha=0.5,color='g')
 ax1.set_ylabel('Performance')
 ax1.set_title('Comparison among models on CpG islands')
 ax1.set_xticks([p + 1 * width for p in pos])
 ax1.set_xticklabels(labels)
 plt.xlim(min(pos)-1.5*width, max(pos)+width*4)
 plt.ylim([0.6,1])
 ax2 = plt.subplot(212)
 plt.bar(pos,p1,width,alpha=0.5,color='b')
 plt.bar([p + width for p in pos],p2,width,alpha=0.5,color='y')
 plt.bar([p + width*2 for p in pos],p3,width,alpha=0.5,color='g')
 ax2.set_ylabel('Performance')
 ax2.set_title('Comparison among models on non-CpG-islands')
 ax2.set_xticks([p + 1 * width for p in pos])
 ax2.set_xticklabels(labels)
 plt.xlim(min(pos)-1.5*width, max(pos)+width*4)
 plt.ylim([0.6,1])
 plt.legend(['MRCNN', 'DeepCpG', 'CNN'], loc='best',fontsize = 'small')
 '''
 You can add more data to make comparison more strong.
 '''
 
 return "Comparison of classification performance of methods:"
 
 
 

 
def tSNEplot(y,z):
 class chj_data(object):
    def __init__(self,data,target):
        self.data=data
        self.target=target
 data = chj_data(fs,lb)
 '''
 Initial parameter setting
 '''
 ff = TSNE(n_components=2,learning_rate=100).fit_transform(data.data)
 plt.figure(figsize=(8, 6))
 plt.subplot(111)           
 x_axis = ff[:, 0]
 y_axis = ff[:, 1]
 plt.figure(figsize=(8, 6))
 plt.scatter(x_axis, y_axis, c=data.target.reshape(385,), marker='o', alpha=0.5)
 plt.title('t-SNE cluster of original representation')
 
 return "t-SNE cluster is as follow:"
 
 
 

 
def linechart(x,ac1,ac2,ac3):
 '''
 For one of the indicators can be drawn as follows, 
 other indicators can be drawn in a similar manner, 
 and will not be described again.
 '''
 plt.subplot(331)
 plt.ylabel('ACC')
 plt.ylim([0.7 ,1])
 new_ticks = np.linspace(1000, 5000, 5)
 print(new_ticks)
 plt.xticks(new_ticks)
 plt.plot(x, ac1, "r-o", label="MRCNN")# use pylab to plot x and y
 plt.plot(x, ac2, "b:*",linewidth=1.5, label="DeepCpG")# show the plot on the screen
 plt.plot(x, ac3, "k--v",linewidth=2, label="Cnn")
 plt.legend(loc="lower right", fontsize = 'small')
 plt.title('test group 1')
 
 return "line chart of different groups tests is as follow:"
 

