class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linkedlist:
	def __init__(self):
		self.start=None
	def AddNodeStart(self,value):
		newnode=node(value)
		if self.start==None:
			self.start=newnode
		else:
			temp=self.start	
			self.start=newnode
			self.start.next=temp
	def ShowList(self):
		temp=self.start
		while(temp!=None):
			print(temp.data,end=" ")
			temp=temp.next		
	def AddNodeEnd(self,value):
		newnode=node(value)
		temp=self.start
		while temp.next!=None:
			temp=temp.next
		temp.next=newnode

	def reverse(self):
		prev=None
		current=self.start
		while current!=None:
			next=current.next
			current.next=prev
			prev=current
			current=next
		self.start=prev
			
	def AddNodeMiddle(self,location,value):
		newnode=node(value)
		temp=self.start
		if location==0:
			print()
			print(self.start.data)
		else:
			for i in range(location-1):
				temp=temp.next
		temp1=temp.next
		temp.next=newnode
		newnode.next=temp1
		#temp
		#print()
		#print(temp.data)	

				


mylist=linkedlist()
mylist.AddNodeStart(1)
mylist.AddNodeStart(2)
mylist.AddNodeStart(3)
mylist.AddNodeStart(4)
mylist.AddNodeEnd(5)
mylist.ShowList()
print()
mylist.AddNodeMiddle(2,7)
#mylist.AddNodeMiddle(1,8)
mylist.ShowList()
mylist.reverse()
print()
mylist.ShowList()