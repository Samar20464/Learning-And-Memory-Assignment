#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy import stats

read1 is 0.75s
read2 is 1.5s
read3 is 3s
read4 is 8s
read5 is 9s
# In[24]:


read1 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None)
read1 = read1.fillna(0)

standard = read1.iloc[2:22,1:101]
deviant = read1.iloc[24:44,1:101]

standMean = standard.mean(axis=0)
stanStd = standard.std(axis=0)
stanMedian = np.median(standard,axis=0)
stanMode = stats.mode(standard)
standvar = np.var(standard,axis =0)

devMean = deviant.mean(axis=0)
devStd = deviant.std(axis=0)
devMedain = np.median(deviant,axis =0)
devMode = stats.mode(deviant)
devVar = np.var(deviant,axis =0)

print("Standard Mean is {}".format(standMean))
print()
print("Standard deviation is {}".format(stanStd))
print()
print("Standard Median is {}".format(stanMedian))
print()
print("Standard Mode is {}".format(stanMode))
print()
print("Standard Variance {}".format(standvar))
print()


print("Deviant Mean is {}".format(devMean))
print()
print("Deviant standard deviation is {}".format(devStd))
print()
print("Deviant Median is {}".format(devMedain))
print()
print("Deviant Mode is {}".format(devMode))
print()
print("Deviant Variance is {}".format(devVar))


# For 1.5s

# In[25]:


read2 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name = 1)
read2 = read2.fillna(0)

standard = read2.iloc[2:22,1:101]
deviant = read2.iloc[24:44,1:101]

standMean = standard.mean(axis=0)
stanStd = standard.std(axis=0)
stanMedian = np.median(standard,axis=0)
stanMode = stats.mode(standard)
standvar = np.var(standard,axis =0)

devMean = deviant.mean(axis=0)
devStd = deviant.std(axis=0)
devMedain = np.median(deviant,axis =0)
devMode = stats.mode(deviant)
devVar = np.var(deviant,axis =0)

print("Standard Mean is {}".format(standMean))
print()
print("Standard deviation is {}".format(stanStd))
print()
print("Standard Median is {}".format(stanMedian))
print()
print("Standard Mode is {}".format(stanMode))
print()
print("Standard Variance {}".format(standvar))
print()


print("Deviant Mean is {}".format(devMean))
print()
print("Deviant standard deviation is {}".format(devStd))
print()
print("Deviant Median is {}".format(devMedain))
print()
print("Deviant Mode is {}".format(devMode))
print()
print("Deviant Variance is {}".format(devVar))


# For 3s

# In[30]:


read3 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name = 2)
read3 = read3.fillna(0)

standard = read3.iloc[2:22,1:101]
deviant = read3.iloc[24:44,1:101]

standMean = standard.mean(axis=0)
stanStd = standard.std(axis=0)
stanMedian = np.median(standard,axis=0)
stanMode = stats.mode(standard)
standvar = np.var(standard,axis =0)

devMean = deviant.mean(axis=0)
devStd = deviant.std(axis=0)
devMedain = np.median(deviant,axis =0)
devMode = stats.mode(deviant)
devVar = np.var(deviant,axis =0)

print("Standard Mean is {}".format(standMean))
print()
print("Standard deviation is {}".format(stanStd))
print()
print("Standard Median is {}".format(stanMedian))
print()
print("Standard Mode is {}".format(stanMode))
print()
print("Standard Variance {}".format(standvar))
print()


print("Deviant Mean is {}".format(devMean))
print()
print("Deviant standard deviation is {}".format(devStd))
print()
print("Deviant Median is {}".format(devMedain))
print()
print("Deviant Mode is {}".format(devMode))
print()
print("Deviant Variance is {}".format(devVar))


# For 8s

# In[29]:


read4 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name = 3)
read4 = read4.fillna(0)

standard = read4.iloc[2:22,1:101]
deviant = read4.iloc[24:44,1:101]

standMean = standard.mean(axis=0)
stanStd = standard.std(axis=0)
stanMedian = np.median(standard,axis=0)
stanMode = stats.mode(standard)
standvar = np.var(standard,axis =0)

devMean = deviant.mean(axis=0)
devStd = deviant.std(axis=0)
devMedain = np.median(deviant,axis =0)
devMode = stats.mode(deviant)
devVar = np.var(deviant,axis =0)

print("Standard Mean is {}".format(standMean))
print()
print("Standard deviation is {}".format(stanStd))
print()
print("Standard Median is {}".format(stanMedian))
print()
print("Standard Mode is {}".format(stanMode))
print()
print("Standard Variance {}".format(standvar))
print()


print("Deviant Mean is {}".format(devMean))
print()
print("Deviant standard deviation is {}".format(devStd))
print()
print("Deviant Median is {}".format(devMedain))
print()
print("Deviant Mode is {}".format(devMode))
print()
print("Deviant Variance is {}".format(devVar))


# For 9s

# In[28]:


read5 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name = 4)
read5 = read5.fillna(0)

standard = read5.iloc[2:22,1:101]
deviant = read5.iloc[24:44,1:101]

standMean = standard.mean(axis=0)
stanStd = standard.std(axis=0)
stanMedian = np.median(standard,axis=0)
stanMode = stats.mode(standard)
standvar = np.var(standard,axis =0)

devMean = deviant.mean(axis=0)
devStd = deviant.std(axis=0)
devMedain = np.median(deviant,axis =0)
devMode = stats.mode(deviant)
devVar = np.var(deviant,axis =0)

print("Standard Mean is {}".format(standMean))
print()
print("Standard deviation is {}".format(stanStd))
print()
print("Standard Median is {}".format(stanMedian))
print()
print("Standard Mode is {}".format(stanMode))
print()
print("Standard Variance {}".format(standvar))
print()


print("Deviant Mean is {}".format(devMean))
print()
print("Deviant standard deviation is {}".format(devStd))
print()
print("Deviant Median is {}".format(devMedain))
print()
print("Deviant Mode is {}".format(devMode))
print()
print("Deviant Variance is {}".format(devVar))


# In[ ]:




