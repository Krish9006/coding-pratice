class Node:
    def __init__(self, item=None, data=None):
        self.item = item
        self.data = data

class SSL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insertFirst(self, data):
        n = Node(data, self.start)
        self.start = n

    def insertlast(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            else:
                return None
        else:
            return None

mylist = SSL()
mylist.insertFirst(1)
mylist.insertlast(8)
mylist.insertFirst(19)
print(mylist)