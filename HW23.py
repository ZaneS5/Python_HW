# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:25:12 2019

@author: Zane
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return 
        else:
            lastNode = self.head
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return 
        else:
            newNode.next = self.head
            self.head = newNode
    def insertAfterNode(self, prevNode, data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        
    def printList(self):
        curNode = self.head
        if curNode == None:
            print("The list is empty")
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next
            
    def deleteNode(self, key):
        curNode = self.head
        if curNode != None and curNode.data == key:
            self.head = curNode.next
            curNode = None
            return
        else:
            prev = None
            while curNode != None and curNode.data != key:
                prev = curNode
                curNode = curNode.next
            if curNode == None:
                print("The data is not found in the list")
                return
            else:
                prev.next = curNode.next
                curNode = None
    def deleteAtPos(self,pos):
        curNode = self.head
        if pos == 0:
            self.head = curNode.next
            curNode = None
            return
        else:
            cnt = 0
            prev = None
            while curNode != None and cnt != pos:
                prev = curNode
                curNode = curNode.next
                cnt += 1
            if curNode == None:
                print("the node doesn't exist")
                return 
            else:
                prev.next = curNode.next
                curNode = None
    def len_iterative(self):
        cnt = 0
        curNode = self.head
        while curNode != None:
            curNode = curNode.next
            cnt += 1
        return cnt
    def swapNode(self, key1, key2):
        if key1 == key2:
            print("The two nodes are the same, they cannot be swapped")
        prev1 = None
        curNode1 = self.head
        while curNode1 != None and curNode1.data != key1:
            prev1 = curNode1
            curNode1 = curNode1.next
        prev2 = None
        curNode2 = self.head
        while curNode2 != None and curNode2.data != key2:
            prev2 = curNode2
            curNode2 = curNode2.next
                
        if curNode1 == None or curNode2 == None: 
            print("The nodes do not ecist in the list")
            return
        else:
            if prev1 == None: # key 1 is in the head ndoe, key2 is not 
                self.head = curNode2
                prev2.next = curNode1
            elif prev2 == None: # key2 is not in th head node, key1 is not 
                self.head = curNode1
                prev1.next = curNode2
            else: # none are the head node
                prev1.next = curNode2
                prev2.next = curNode1
            temp1 = curNode1.next
            temp2 = curNode2.next
            curNode1.next = temp2
            curNode2.next = temp1
    def reverse_iterative(self):
        prev = None
        curNode = self.head
        while curNode != None:
            nxt_temp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nxt_temp
        self.head = prev
    def Delete(self):
       self.head = None
    def length(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count
            
            
            
        
lst = linkedList()
lst.append('A')
lst.append('B')
lst.append('C')
lst.prepend('D')
print("List Length is:", lst.length())
lst.reverse_iterative()
lst.printList()
print('\n')
lst.Delete()
lst.printList()


#print("Initialization Test:")                
#myList = linkedList()
#myList.append("This is my list")
#myList.printList()
#print('\n')
#myList.prepend("This is Zane's list")
#print("Prepend Test:")
#myList.printList()
#print('\n')
#temp = myList.head.next
#print("insertAfterNode Test:")
#myList.insertAfterNode(temp, "=^_^=")
#myList.printList()
#print('\n')
#print("deleteNode Test:")
#myList.deleteNode("This is my list")
#myList.printList()
#print('\n')
#print("deleteAtPos Test:")
#myList.deleteAtPos(0)
#myList.printList()
#print('\n')
#myList.append("( ͡° ͜ʖ ͡°)")
#myList.printList()
#print('\n')
#myList.swapNode("( ͡° ͜ʖ ͡°)", "=^_^=")
#print("swapNode Test:")
#myList.printList()
#print('\n')




















