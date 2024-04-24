class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,b):
        return complex(self.real + b.real ,self.img + b.img)
a=complex(5,6)
b=complex(4,6)
c=a+b
print(c.real,c.img)
        
        