class Node:
    def __init__(self,item= None,data=None):
        self.item=item
        self.data=data
class SSL: 
    def __init__(self,start=None):
        self.start =start 
        def __is_empty(Self):
            return self.start==None
    def __insertFirst(self,data):
        n=Node(data,self.start)
        self.start=n
    def __insertlast(self,data):
        n=Node(data)
        if  not self.start .is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                temp=next=n
            else:
                self.start=n
    def __search(self,data):
        if not self.start.is_empty():
            temp=self.start
            while temp.next is not None:
                if temp.item==data:
                    return temp
                temp=temp.next
            else:
                return None
        else:
            return None
        


        

mylist=SSL()