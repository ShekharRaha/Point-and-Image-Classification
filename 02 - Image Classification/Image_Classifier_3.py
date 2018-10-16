
# coding: utf-8

# In[1]:


# Improving the performance


# In[2]:


# Importing the libraries

import numpy as np    # For scientific computing
import matplotlib.pyplot as plt    # For generating plots
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


from sklearn import datasets
digits = datasets.load_digits()


# In[4]:


# Enlarge training data from 10 to 1000 images

X_train = digits.data[0:1000]
Y_train = digits.target[0:1000]


# In[5]:


# Function to classify images using the nearest neighbour classifier

def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


# In[6]:


# Number of mistakes done in testing 100 images

num = len(X_train)
no_errors = 0
distance = np.zeros(num)

for j in range(1697, 1797):
    X_test = digits.data[j]
    
    for i in range(num):
        distance[i] = dist(X_train[i], X_test)
        
    min_index = np.argmin(distance)
    
    # Counting the errors:
    if Y_train[min_index] != digits.target[j]:
        no_errors += 1


# In[7]:


# Printing the number of errors

print(no_errors)

