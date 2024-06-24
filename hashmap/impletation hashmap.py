class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
 class ht:
    def __init__(self):
        self.size = 0
        self.capacity = 5
        self.data =[[]for i in range(self.capacity)]
    def getsize(self):
        return self.size
    def insert(key,value):
        entry = Entry(key,value)
        index = entry.hash % self.capacity
        isupdated=False
        for i in  range(len(self.data[index])):
            if (self.data[index][i].key==key):
                self.data[index][i]=entry
                break