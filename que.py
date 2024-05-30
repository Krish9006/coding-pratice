class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def size(self):
        count = 0
        temp = self.front
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def is_empty(self):
        temp = self.front
        if temp is None:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data)
        else:
            temp = self.rear
            temp.next = Node(data)
            self.rear = temp.next

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def __str__(self):
        result = []
        temp = self.front
        while temp is not None:
            result.append(str(temp.data))
            temp = temp.next
        return " <-> ".join(result)