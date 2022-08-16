#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Searching Algorithms

#linear search

#array = [10,20,30,40,50]
#target=80
#return its index
#if target value is not present then we need to return -1

#output:1


def linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            print("Element is present at index",i)
            break
    else:
        print("Element is not present or -1")
array=[10,20,30,40,50]
target=48
linear_search(array,target)


# In[ ]:





# In[ ]:




