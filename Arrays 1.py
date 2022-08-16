#!/usr/bin/env python
# coding: utf-8

# In[15]:


a=list()
a.append(20)
print(a)


# In[29]:


#implements operation of arrays
class arrays:
    def __init__(self):
        self.array=[]
    def insert_at_begin(self,data):
        self.array.insert(0,data)
        return self.array
    def insert_at_last(self,data): #insert(len(self.array)-1,data)
        self.array.append(data)
        return self.array
    def insert_at_pos(self,data,i):
        if i>len(self.array):
            return self.array
        self.array.insert(i,data)
        return self.array
    def remove_at_begin(self):
        if len(self.array)<1:
            return self.array  # del self.array[0]
        self.array.pop(0)
        return self.array
    def remove_at_last(self):
        if len(self.array)<1:
            return self.array
        self.array.pop()
        return self.array
    def remove_at_pos(self,i):
        if i>len(self.array) and len(self.array)<1:
            return self.array
        self.array.pop(i)
        return self.array
    def traverse(self):
        for i in range(len(self.array)):
            print(self.array[i])
    
        
        
        
    
s=arrays()
s.insert_at_begin(10)#10
s.insert_at_begin(20) #20 10
s.insert_at_begin(30) #30 20 10
s.insert_at_begin(40) #40,30,20,10
s.insert_at_pos(100,1)
s.insert_at_last(2000)
s.remove_at_begin()
s.remove_at_last()
s.remove_at_pos(2)
s.traverse()


            



# In[ ]:





# In[ ]:




