#7.Use appropriate functions for each classWrite a program to display MRO using multiple inheritance. Multiple inheritance can be done as per your choice. 

class P:
    def showA(self):
        print("Class P Method")

class Q:
    def showB(self):
        print("Class Q Method")

class R(P, Q):
    def showC(self):
        print("Class R Method")

obj = R()
obj.showA()
obj.showB()
obj.showC()

print("Method Resolution Order:")
print(R.__mro__)