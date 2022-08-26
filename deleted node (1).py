#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printll(head):
    while head is not None:
        print((head.data),end="")
        head=head.next
    print("None")
def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
 
def insert_at_po(head,data,i=0):
    if i<0 and i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count=count+1
    newNode=Node(data)
    if prev is None:
        newNode.next=curr
        head=newNode
    else:
        prev.next=newNode
        newNode.next=curr
    return head
def deleted(head,i):
    if i==0:
        head=head.next
    else:
        count=1
        curr=head
        while count<i:
            curr=curr.next
            count=count+1
        curr.next=curr.next.next
    return head
 
 
 
node1=Node(100)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4
printll(node1)
x = deleted(node1,0)#length(node1)-1
printll(x)


# In[ ]:




