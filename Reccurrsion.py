#FACTORIAL OF A NUMBER

'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))''' 



#TABLE

def table(n):
    c=0
    if n==10:
        return 1
    else:
        print(c)
        c=n*table(n+1)
table(1)        