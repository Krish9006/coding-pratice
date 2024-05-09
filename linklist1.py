class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.__prev=prev
        self.__next=next
class DLL:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    def size(self):
        return self.__size
    def isEmpty(self):
        return self.size()==0 
    def append(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode 
            self.__tail=newNode
        else:
            self.__tail.next=newNode
            newNode.prev=self.__tail
            self.__tail-newNode
            self.size+=1
    def __str__(self):
        l=[]
        trav= self.__head
        while trav is not None:
            l.append(trav.data)
            trav=trav.__next
        return '<--->'.join(map(str,l))
    
    def addfirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            newNode.next=self.__head
            self.__head.prev=newNode
            self.__head=newNode
            self.size+=1
    def addAT(index,data):
                if index<0 or index>self.size:
                    raise Exception("invalid index")
                if index==0:
                    self.addfirst(data)
                elif index==self.size:
                    self.append(data)   
                else:
                    id =0
                    trav=self.__head
                    while id<index-1:
                        trav=trav.next
                        id+=1
                        trav= trav.next
                        newNode = Node(data,trav,trav.next)
                        trav.next=newNode
                        newNode.next.prev=newNode
                        size+=1
    def removefirst(self):
        temp=self.__head
        self.__head =self.__head.next
        self.__head.preb                        

            

l=DLL()
print(l.size())
print(l.isEmpty())
l.append(10)
l.append(20)
l.append(30)
print(l.size())
print(l.__str__())
l.addfirst(5)
l.addfirst(15)
print(l.__str__())
l.addAT(2,12)
print(l.__str__())
