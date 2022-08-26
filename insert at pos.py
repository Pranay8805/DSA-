#!/usr/bin/env python
# coding: utf-8

# In[52]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #next

def printall(head):
    while head is not None:
        print(str(head.data)+"->",end=" ") #traversal of linkedlist
        head=head.next
    print("None")
def lenght(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
        
def insert_at_pos(head,i,data):
    if i<0 and i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<1:
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
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2 # make connection # node2.next=node1 
node2.next=node3
node3.next=node4
printall(node1) 
x=insert_at_pos(node1,0,300)
printall(x)
        


# In[53]:


def lenght(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count


# In[43]:





# In[ ]:





# In[ ]:





# In[ ]:




