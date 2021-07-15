#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


# In[9]:


pip install opencv-python==3.4.2.17


# In[2]:


import cv2


# In[60]:



'''
data_dir ='/Users/nooreen/Downloads/kagglecatsanddogs_3367a/PetImages'
categories = ['cat','dog']
'''


# In[3]:


raw_data_dir='/Users/nooreen/Desktop/data/raw_data'
categories =['black','white','blue','green','grey','brown','purple','pink','yellow','orange']


# In[4]:



from PIL import Image


# In[5]:


for catagory in categories:
    #path = data_dir +'/'+ str(catagory)
    path = os.path.join(raw_data_dir,catagory) #gets path to directory
    print(len(os.listdir(path)))
    for img in os.listdir(path):
        
        image = Image.open(path+'/'+img)
        image = image.resize((20,20))
        #plt.imshow(image)
        new_path = '/Users/nooreen/Desktop/data/preprocessed/'+ catagory +'/'+ img
       
        image.save(new_path,'png')
        
       
    


# In[ ]:




