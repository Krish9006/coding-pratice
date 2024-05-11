class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
            self.__size += 1

    def __str__(self):
        l = []
        trav = self.__head
        while trav is not None:
            l.append(trav.data)
            trav = trav.next
        return '<--->'.join(map(str, l))

    def addfirst(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode
            self.__size += 1

    def addAT(self, index, data):
        if index < 0 or index > self.size():
            raise Exception("invalid index")
        if index == 0:
            self.addfirst(data)
        elif index == self.size:
            self.append(data)
        else:
            id = 0
            trav = self.__head
            while id < index - 1:
                trav = trav.next
                id += 1
            newNode = Node(data, trav, trav.next)
            trav.next = newNode
            newNode.next.prev = newNode
            self.__size += 1

    def removefirst(self):
        temp = self.__head
        self.__head = self.__head.next
        self.__head.prev = None

l = DLL()
print(l.size())
print(l.isEmpty())
l.append(10)
l.append(20)
l.append(30)
print(l.size())
print(l)
l.addfirst(5)
l.addfirst(15)
print(l)
l.addAT(2, 12)
print(l)