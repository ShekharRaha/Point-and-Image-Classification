
# coding: utf-8

# In[1]:


# Point Classification


# In[2]:


# Importing the libraries

import numpy as np    # For scientific computing
import matplotlib.pyplot as plt    # For plotting graphs
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


# Create training set containing points and labels(colours)

X_train = np.array([[1, 1], [2, 2.5], [3, 1.2], [5.5, 6.3], [6, 9], [7, 6]])
Y_train = ['red', 'red', 'red', 'green', 'green', 'green']


# In[4]:


# Plot the training set

plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], s = 170, color = Y_train[:])
plt.show()


# In[5]:


# Create a new test point

X_test = np.array([3, 4])


# In[7]:


# Plotting the new test point

plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], s = 170, color = Y_train[:])
plt.scatter(X_test[0], X_test[1], s = 170, color = 'blue')
plt.show()


# In[8]:


# Function to run the nearest neighbour classifier

def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


# In[9]:


# For each point in X_train we compute its distance to X_test

num = len(X_train)    # number of points in X_train
distance = np.zeros(num)    # numpy array of zeros

for i in range(num):
    distance[i] = dist(X_train[i], X_test)


# In[10]:


# Choose the point in X_train with the minimal distance from X_test

min_index = np.argmin(distance)    # Index with smallest distance


# In[11]:


# Print the colour of the point closest to X_test

print(Y_train[min_index])

