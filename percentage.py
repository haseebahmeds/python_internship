sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
a=((sub1+sub2+sub3+sub4+sub5)/500)*100
if(a>75):
    print("grade A")
elif(a>60 and a<74):
    print("grade B")
elif(a>35 and a<59):
    print("grade c")
else:
    print("fail")