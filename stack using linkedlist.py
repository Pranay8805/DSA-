#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Stack Using Linkedlist
Operations:
 1.Push -> insertion of element at the top(adding of element)
 2.Pop->Deletion of element from the top(deletion of element)
 3.Peek -> Will return you the top value first element value 


# In[ ]:


count = 0
push operation:
    create a node --> newNode=Node(data)
    make connection---> newNode.next=head
    change head---> head=newNode
    councount+1
pop operation:
    head=head.next
    count=count-1


# In[11]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.count=0
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        self.count+=1
    def pop(self):
        if self.count==0:
            print("Stack is empty")
            return
        temp=self.head.data
        self.head=self.head.next
        self.count-=1
        return temp
    def peek(self):
        if self.count==0:
            print("Stack is empty")
            return
        return self.head.data
s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())

print(s.pop())
print(s.peek())


# In[ ]:





# In[ ]:




