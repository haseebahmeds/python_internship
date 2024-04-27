def isprime(n):
     for i in range(2,a-1):
       if(a%i==0):
         return false
     else:
      return true       
a=int(input())
b=int(input())
for i in range(a,b+1):
   if isprime(a):
      print("prime")
else:
   print("true")