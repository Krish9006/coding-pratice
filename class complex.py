class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,b):
        return complex(self.real + b.real ,self.img + b.img)
    
    def __sub__(self,b):
        return complex(self.real - b.real ,self.img - b.img)
    def __mul__(self,b):
        return complex(self.real  b.*real ,self.img * b.img)
    def __divide__(self,b):
        return complex(self.real  b./real ,self.img / b.img)


a=complex(5,6)
b=complex(4,6)
c=a+b
d=a-b
e=a*b
f=a/b


print(c.real,c.img)
print(d.real,d.img)
print(e.real,e.img)
        
        