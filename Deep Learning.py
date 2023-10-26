#!/usr/bin/env python
# coding: utf-8

# import keras

# from keras.models import Sequential

# model = Sequential()

# from keras.layer import Dense

# n_cols = concrete_data.shape[1]

# model.add(Dense(5, activation='ReLu', input_shape=(n_cols,)))
# model.add(Dense(5, activation="Relu"))
# model.add(Dense(1))

# In[1]:


x_1 = 0.1
w_1 = 0.15
b_1 = 0.40
w_2 = 0.45
b_2 = 0.65
z_1 = x_1 * w_1 + b_1
z_1


# In[ ]:





# In[2]:


import statistics
import math
from statistics import exp


# In[3]:


#Find the output using Sigmoid Function
a_1 = 1/(1+exp(-z_1))
a_1


# In[4]:


z_2 = a_1 * w_2 + b_2
z_2


# In[5]:


#Find the ouput using sigmoid function
a_2 = 1/(1+exp(-z_2))
a_2


# In[6]:


z_1,a_1,z_2,a_2


# In[7]:


T = 0.25
epochs = 1000
nu = 0.4
Ee= 0.001


# In[8]:


import numpy as np


# In[9]:


E = 1/2*((T-a_2)**2)
E


# In[10]:


#Uodate w_2 
w_2_2 = w_2 - nu * (a_2 - T) * (a_2 - (a_2)**2) * a_1
w_2_2


# In[11]:


#Uodate b_2 
b_2_2 = b_2 - nu * (a_2 - T) * (a_2 - (a_2)**2) * 1
b_2_2


# In[12]:


#Uodate w_1
w_1_1 = w_1 - nu * (a_2 - T) * (a_2 - (a_2)**2) * w_2 * (a_1 - (a_1)**2) * x_1
w_1_1


# In[13]:


#Update b_1 
b_1_1 = b_1 - nu * (a_2 - T) * (a_2 - (a_2)**2) * w_2 * (a_1 - (a_1)**2) * 1
b_1_1


# In[14]:


#All the update points
print("The update of w_1 is :", w_1_1,"\n","The update of w_2 is :", w_2_2,"\n","The update of b_1 is :",b_1_1,"\n","The update of b_2 is :",b_2_2)


# In[ ]:





# In[ ]:





# In[15]:


#Find the output using hyperbolic tangente function
a_22 = ((exp(z_1)) - (exp(-z_1))) / ((exp(z_1)) + (exp(- z_1)))
a_22


# In[16]:


#Find the ouput using ReLu function
a_23 = max(0, z_1)
a_23


# In[ ]:





# In[17]:


z_t = 0.2675
a_t = 1/(1+exp(-z_t))
a_t


# In[18]:


xx_1 = 0.25
ww_1 = 0.15
ww_3 = 0.25
ww_4 = 0.55
xx_2 = 0.05
ww_2 = 0.45
bb_1 = 0.45
bb_2 = 0.25
ww_5 = 0.50
ww_6 = 0.60

zz_1 = xx_1 * ww_1 + xx_2 * ww_2 + bb_1
zz_1


# In[19]:


z_1_2 = xx_1 * ww_3 + xx_2 * ww_4 + bb_1
z_1_2


# In[20]:


a_1_2 = 1/(1+exp(-z_1_2))
a_1_2


# In[21]:


z_2_1 = xx_1 * ww_5 + a_1_2 * ww_6 + bb_2
z_2_1


# In[22]:


a_2_2 = 1/(1+exp(-z_2_1))
a_2_2


# In[23]:


tt_11 = 0.15
tt_22 = 0.85
ttot = tt_11 + tt_22
ttot


# In[24]:


E = 1/2*((T-a_2)**2)
E


# In[ ]:





# In[ ]:




