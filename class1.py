print("Welcome to Python Class")
print("Kamran Ahmed")

name : str = "Kamran Ahmed"
print(name)   # print
print(type(name))   # type
print(id(name)) # physical address
print([i for i in dir(name)])   # Methods and Attributes


name : tuple[str,int,float,bool] = ("Daniyal", 5000, 15.653, True)
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name)])

name : any = "Daniyal"
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name)])
