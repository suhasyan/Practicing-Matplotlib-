#!/usr/bin/env python
# coding: utf-8

# # 1.WHAT IS MATPLOTLIB?

# Matplot is a popular data visualization library in python that provides a wide range of ploting functions and tools.It allows data scientists to creat high-quality charts,graphs,and visualization with ease.

# # 2.WHY USE MATPLOTLIB IN DATA SCIENCE?

# Matplot is widely used in data science due to its flexibility,extensive functionality,and compatibility with other libraries like Numpy and Pandas.It offers a vast arry of plot types,customization options,and excellent documentation,making it an essential tool for data exploration and presentation.

# In[ ]:


#Installing Matplotlib
pip install matplotlib


# In[2]:


#Importing Matplotlib
import matplotlib.pyplot as plt


# # Basic Plots

# In[3]:


# 1.Line Plot

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Plot')
plt.show()


# In[4]:


# 2.Scatter Plot

x=(1,2,3,4,5)
y=(2,4,6,8,10)

plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.show()


# In[12]:


# 3.Bar Plots

categories = ['A','B','C','D','E']
values = [10,20,30,40,50]

plt.bar(categories,values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bra Plot')
plt.show()


# In[10]:


# 4.Histograms

import numpy as np

data = np.random.randn(1000)  #Generate random data
plt.hist(data,bins=500)
plt.xlabel('values')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()


# # Customizing Plots
#  

# In[16]:


# Figure size and Resolution

plt.figure(figsize=(8,6), dpi=100)
# create and customize your plot
plt.show()


# In[17]:


# Labels and Titles


plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Plot')
plt.show()


# In[29]:


# Colors,Styles,and Makers

plt.plot(x,y, color='red',linestyle='--',marker='8')
plt.show()


# In[30]:


# Axis Limits and Ticks

plt.plot(x,y)
plt.xlim(0,10)
plt.ylim(0.20)
plt.xticks([0,5,10])
plt.yticks([0,10,20])
plt.show


# <!-- # Multiple Subplots  -->

#  # Multiple Subplots:

# In[34]:


# Creating Subplots

fig, axes = plt.subplots(nrows=2,ncols=2)
ax1,ax2,ax3,ax4 = axes.flatten()

ax1.plot(x,y)
ax2.scatter(x,y)
ax3.bar(categories,values)
ax4.hist(data,bins=30)
plt.show()


# In[35]:


# Customizing Subplots

fig, axes = plt.subplots(nrows=2,ncols=2)
ax1,ax2,ax3,ax4 = axes.flatten()

ax1.plot(x,y)
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')

ax2.scatter(x,y)
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')

# customizing other subplots
plt.show()


# In[36]:


# sharing Axis Labels

fig,axes=plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True)
ax1,ax2,ax3,ax4 = axes.flatten()
plt.show()


# # Advanced Plots

# In[39]:


# Pie Charts

sizes = [20,30,15,10]
labels =['A','B','C','D']

plt.pie(sizes,labels=labels, autopct='%1.if%%')
plt.title('Pie Chart')
plt.show()


# In[40]:


# Box Plots

data = [np.random.normal(0,std,100)for std in range(1,4)]

plt.boxplot(data)
plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()


# In[42]:


# Heat Maps

data=np.random.random((10,20))

plt.imshow(data, cmap='hot',interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()


# In[44]:


# 3D pLOTS

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y =np.meshgrid(x,y)
Z=np.sin(np.sqrt(Y**2+Y**2))

ax.plot_surface(X,Y,Z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.title('3D PLOT')
plt.show()


# # Conclusion

# Matplotlib is a powerful and versatile data visualization library
#  for Python. In this guide, we covered the basics of Matplotlib
#  and explored various plot types, customization options, and
#  advanced features. By following this practical guide, you
#  should now be equipped with the knowledge and tools to
#  create visually appealing and informative plots for your data
#  science projects. Experiment with different plot types and
#  customization options to unleash the full potential of
#  Matplotlib. Happy plotting

# # Thank you

# In[ ]:




