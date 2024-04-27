#single inheritance

class a:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2") 

class b(a):
    def __init__(self):
        print("1")
    def __init__(self):
        print("2")
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun 4")
class c:
    pass
o=a()
p=b()
p.fun1()
o.fun2()
p.fun3()
p.fun4()

