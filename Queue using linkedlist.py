#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Queue using linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.count=0
        self.tail=None
    def enqueue(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            self.tail.next=newNode
        self.tail=newNode
        self.count+=1
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return
        temp=self.head.data
        self.head=self.head.next
        self.count-=1
        return temp
    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return
        return self.head.data
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.peek())


# In[ ]:




