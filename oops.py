1)
class employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount+=1
    def displaycount(self):
        print("Total=",employee.empcount)
    def displayemployee(self):
        print("name=",self.name,"salary=",self.salary)
emp1=employee("python",5200)
emp1.displayemployee()
emp1.displaycount()
2)
class abc:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name_
        print(class_name,"destroyed")
ptr1=abc()
ptr2=ptr1
ptr3=ptr1
print(id(ptr1),id(ptr2),id(ptr3))
del ptr1
del ptr2
del ptr3
3)
class parent:
    parentattr=100;
    def __init__(self):
        print("calling parent counter")
    def parentmethod(self):
        print("calling parent method")
    def setattr(self,attr):
        parent.parentattr=attr
    def getattr(self):
            print("print attribute=",parent.parentattr)
class child(parent):
     def __init__(self):
         print("calling child constructor")
     def childmethod(self):
        print("calling child method")
c=child()
c.childmethod()
c.parentmethod()
c.setattr(200)
c.getattr()

