#!/usr/bin/env python
# coding: utf-8

# In[30]:


#linkedlist:
#linkedlist: it is a linear data structure that has collection of nodes .
#Nodes: it is a combination of data and address

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #address

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
#print(node1.data)
#print(node1.next)#initially none 
node1.next=node2 # make connection # node2.next=node1 
node2.next=node3
node3.next=node4  # all 4 are connected with each other
print(node1.next) #address           node2  print(node 1)
print(node2.next)
#print(node3.next)
print(node2)#   address of node 1 and node 2 is same and the coonection is implemented
print(node3)
#print(node2.data)
#print(node3.data)
#print(node4.data)



# In[31]:


# printing all linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.address=None #next

def printall(head):
    while head is not None:
        print(head.data,end=" ") #traversal of linkedlist
        head=head.address
        
def insertion_at_begin(head,data): #creating new node in the beginning
    newnode=Node(data)
    newnode.address=head
    head=newnode
    return head
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.address=node2 # make connection # node2.next=node1 
node2.address=node3
node3.address=node4
printall(node1)
x=insertion_at_begin(node1,100)
print("--------------------")
printall(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




