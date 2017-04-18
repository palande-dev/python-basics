''' Create and Display Linked List '''



class LinkedList:                             
  
  def __init__(self):
    self.head = None
    
  ''' addData will store the newest value of node in newNode and point newNode to the head node which is initially set to Null. after that the newNode will conatin value of head node and go on appendig values at its back'''


  def addData(self,data):
      newNode = Node (data)
      if self.head == None: 
        self.head = newNode 
      else:
        newNode.setNext(self.head)
        self.head = newNode 
        
  
    
  def isEmpty(self):
    return self.head == None
    
  def printLinkedList(self):
    node = self.head
    while node != None :
      print node.getData()
      node = node.getNext()
      
      
  def length(self):
    count = 1
    curr = self.head
    while curr.next != None:
      curr = curr.next
      count = count +1
    return count
    
  ''' To append data at the end of LinkedList '''  
  def append(self,data):
    newADD = Node(data)
    curr = self.head
    while curr.next != None:
      curr = curr.next
      
    curr.next = newADD
    #newADD.next = None
    
  ''' To insert data at the kth position in the LinkedList '''
  def insertAt(self,data,pos):
    newNode = Node(data)
    count = 1
    curr = self.head
    while curr.next != None and count < pos:
      count = count + 1
      if count == pos:
        newNode.next = curr.next
        curr.next = newNode
      curr = curr.next
	  
  def deleteElement(self, data):
    count = 1
    curr = self.head
    while curr.next != None and curr.data < data:
      count = count + 1
      if count == pos:
        curr.next = curr.next.next
      curr = curr.next
    
   

class Node: 
    def __init__(self,initdata):
      self.data = initdata
      self.next = None
    
    def setData(self,newData):
      self.data = newData
  
    def setNext(self, newNext):
      self.next = newNext
    
    def getData(self):
      return self.data
    
    def getNext(self):
      return self.next
    
    
Mylist = LinkedList()
print Mylist.isEmpty()
Mylist.addData(5)
Mylist.addData(4)
Mylist.addData(3)
Mylist.addData(2)
Mylist.addData(1)
Mylist.printLinkedList()
#print Mylist.isEmpty()
print "lenght is ",Mylist.length()
print Mylist.append(101)
print "lenght is after appending  ",Mylist.length()

Mylist.printLinkedList()
Mylist.insertAt(202,3)
print "lenght is after inserting  ",Mylist.length()
Mylist.printLinkedList()
    