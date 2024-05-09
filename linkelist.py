class node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):
        return (f"data is {2*self.data}")
node= node(10)
print(node)
print(node.data)