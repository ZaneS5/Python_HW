# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:37:49 2019

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
            while lastNode != None:
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
                
print("Initialization Test:",)                
myList = linkedList()
myList.append("This is my list")
myList.printList()
print('\n')
myList.prepend("This is Zane's list")
print("Prepend Test:")
myList.printList()
print('\n')
temp = myList.head.next
print("insertAfterNode Test:")
myList.insertAfterNode(temp, "=^_^=")
myList.printList()
print('\n')
print("deleteNode Test:")
myList.deleteNode("This is my list")
myList.printList()


























