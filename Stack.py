#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Stack

Stack: stack is a linear data structure that follows the principle LIFO(last in last out)
       in stack insertion and deletion both will done from the top.
        How we can implement a stack:
            1.using array
            2.using linkedlist

Operations:
    1.Push-> insertion of element at the top (adding of element)
    2.Pop->Deletion of element from the top (deleation of element)
    3.Peek->Will return you the top value first element value


# In[11]:


#Using Array

class Stack:
    def __init__(self):
        self.data=[]
    def push(self,item):
        self.data.append(item)
    def pop(self):
        if len(self.data)==0:
            print("Stack is Empty")
            return
        return self.data.pop()
    
    def peek(self):
        if len(self.data)==0:
            print("Stack is Empty")
            return
        return self.data[len(self.data)-1]
    
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())
print(s.pop())

print(s.peek())



# In[ ]:





# In[ ]:





# In[ ]:




