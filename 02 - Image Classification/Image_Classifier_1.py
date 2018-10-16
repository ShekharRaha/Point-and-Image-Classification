
# coding: utf-8

# In[1]:


# Image Classifying for single image


# In[2]:


# Importing the libraries

import numpy as np    # For scientific computing
import matplotlib.pyplot as plt    # For generating plots
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


# Load the digits dataset from sklearn

from sklearn import datasets
digits = datasets.load_digits()


# In[4]:


# Plotting a figure

plt.figure()
plt.imshow(digits.images[0], cmap = plt.cm.gray_r, interpolation = 'nearest')
plt.show()


# In[5]:


# Print true label (Checking the correct output)

print(digits.target[0])


# In[6]:


# Creating the training set by choosing the first 10 images in the dataset

X_train = digits.data[0:10]
Y_train = digits.target[0:10]


# In[7]:


# Creating a test image

X_test = digits.data[345]


# In[8]:


# Plotting

plt.figure()
plt.imshow(digits.images[345], cmap = plt.cm.gray_r, interpolation = 'nearest')
plt.show()


# In[9]:


# Function to classify images using the nearest neighbour classifier

def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


# In[10]:


# Running the nearest neighbour classifier

num = len(X_train)
distance = np.zeros(num)

for i in range(num):
    distance[i] = dist(X_train[i], X_test)

min_index = np.argmin(distance)
print(Y_train[min_index])


# In[11]:


# Checking the correct output

print(digits.target[min_index])

