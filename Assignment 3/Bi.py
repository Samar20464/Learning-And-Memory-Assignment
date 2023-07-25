#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

read1 is 0.75s
read2 is 1.5s
read3 is 3s
read4 is 8s
read5 is 9s
# In[2]:


read1 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None)
read1 = read1.fillna(0)
read1


# In[3]:


read2 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name =1)
read2 = read2.fillna(0)
read2


# In[4]:


read3 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name =2)
read3 = read3.fillna(0)
read3


# In[5]:


read4 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name =3)
read4 = read4.fillna(0)
read4


# In[29]:


read5 = pd.read_excel('Assignment3-Q2Bdata.xls',header=None,sheet_name =4)
read5 = read5.fillna(0)
read5


# In[7]:


arr1 =[]
for i in range(2,22):
    arr1.append(np.mean(read1.iloc[i,1:101].to_numpy()))
arr1


# In[8]:


stand075 =  read1.iloc[2:22,1:101].to_numpy()
dev075 =  read1.iloc[24:44,1:101].to_numpy()


# In[9]:


arr2=[]
for i in range(24,44):
    arr2.append(np.mean(read1.iloc[i,1:101].to_numpy()))
arr2


# In[10]:


stanMean075 = np.mean(stand075,axis =0)
dev075Mean = np.mean(dev075,axis=0)

stanMean075


# In[11]:


stan15 =  read2.iloc[2:22,1:101].to_numpy()
dev015 =  read2.iloc[24:44,1:101].to_numpy()


# In[12]:


arr3=[]
for i in range(2,22):
    arr3.append(np.mean(read2.iloc[i,1:101].to_numpy()))
arr3


# In[13]:


arr4=[]
for i in range(24,44):
    arr4.append(np.mean(read2.iloc[i,1:101].to_numpy()))
arr4


# In[14]:


stanMean15 = np.mean(stan15,axis=0)
dev15Mean = np.mean(dev015,axis=0)
stanMean15


# In[15]:


stan3 =  read3.iloc[2:22,1:101].to_numpy()
dev3 =  read3.iloc[24:44,1:101].to_numpy()


# In[16]:


arr5=[]
for i in range(2,22):
    arr5.append(np.mean(read3.iloc[i,1:101].to_numpy()))
arr5


# In[17]:


arr6=[]
for i in range(24,44):
    arr6.append(np.mean(read3.iloc[i,1:101].to_numpy()))
arr6


# In[18]:


stanMean3 = np.mean(stan3,axis=0)
dev3Mean = np.mean(dev3,axis=0)


# In[19]:


stan8 =  read4.iloc[2:22,1:101].to_numpy()
dev8 =  read4.iloc[24:44,1:101].to_numpy()


# In[20]:


arr7=[]
for i in range(2,22):
    arr7.append(np.mean(read4.iloc[i,1:101].to_numpy()))
arr7


# In[21]:


arr8=[]
for i in range(24,44):
    arr8.append(np.mean(read4.iloc[i,1:101].to_numpy()))
arr8


# In[22]:


stanMean8 = np.mean(stan8,axis=0)
dev8Mean = np.mean(dev8,axis=0)


# In[23]:


stan9 =  read5.iloc[2:22,1:101].to_numpy()
dev9 =  read5.iloc[24:44,1:101].to_numpy()


# In[24]:


arr9=[]
for i in range(2,22):
    arr9.append(np.mean(read5.iloc[i,1:101].to_numpy()))
arr9


# In[25]:


arr10=[]
for i in range(24,44):
    arr10.append(np.mean(read5.iloc[i,1:101].to_numpy()))
arr10


# In[26]:


stanMean9 = np.mean(stan9,axis=0)
dev9Mean = np.mean(dev9,axis=0)
stanMean9


# In[27]:


dev9Mean


# In[28]:


fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(8, 10))


axs[0].plot(arr1, color='blue', label='Standard')
axs[0].plot(arr2, color='red', label='Deviant')
axs[0].set_title('ISI = 0.75 s')
axs[0].legend()

axs[1].plot(arr3, color='blue', label='Standard')
axs[1].plot(arr4, color='red', label='Deviant')
axs[1].set_title('ISI = 1.5 s')
axs[1].legend()

axs[2].plot(arr5, color='blue', label='Standard')
axs[2].plot(arr6, color='red', label='Deviant')
axs[2].set_title('ISI = 3 s')
axs[2].legend()

axs[3].plot(arr7, color='blue', label='Standard')
axs[3].plot(arr8, color='red', label='Deviant')
axs[3].set_title('ISI = 8 s')
axs[3].legend()

axs[4].plot(arr9, color='blue', label='Standard')
axs[4].plot(arr10, color='red', label='Deviant')
axs[4].set_title('ISI = 9 s')
axs[4].legend()


plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




