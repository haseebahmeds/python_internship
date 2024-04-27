'''class cse:
    def __init__(self,name,rollno):
      self.n=name
      self.rn=rollno

    def fun(s):
        print(s.n,s1.rn)
s1=cse('rahul',34)
s2=cse('haseeb',36)
s1.fun()
s2.fun()
print(s1.n,s2.rn)'''

'''import math
class circle:
    def __init__(self,radius):
        self.r=radius
    def printing(self):
        print(math.pi*self.r*self.r)
class rectangle:
     def __init__(self,l,b):
        self.l=l
        self.b=b
     def printing(self):
        print(self.l*self.b)
l=float(input())        
b=float(input())        
r=float(input())
o=circle(r)  
o1=rectangle(l,b) 
o.printing()     
o1.printing()     '''



'''class re:
    def __init__(self,name,color,mileage):
        self.name=name
        self.cl=color 
        self.m=mileage
a=re("classic 350","pink",10)        
b=re("access 125","black",65)        
c=re("Ntorq","yellow",30)   
print(a.name,a.cl,a.m)     
print(b.name,b.cl,b.m)     
print(c.name,c.cl,c.m)'''


'''import turtle 

# Creating a turtle object(pen) 
pen = turtle.Turtle() 

# Defining a method to draw curve 
def curve(): 
	for i in range(200): 

		# Defining step by step curve motion 
		pen.right(1) 
		pen.forward(1) 

# Defining method to draw a full heart 
def heart(): 

	# Set the fill color to red 
	pen.fillcolor('red') 

	# Start filling the color 
	pen.begin_fill() 

	# Draw the left line 
	pen.left(140) 
	pen.forward(113) 

	# Draw the left curve 
	curve() 
	pen.left(120) 

	# Draw the right curve 
	curve() 

	# Draw the right line 
	pen.forward(112) 

	# Ending the filling of the color 
	pen.end_fill() 

# Defining method to write text 
def txt(): 

	# Move turtle to air 
	pen.up() 

	# Move turtle to a given position 
	pen.setpos(-68, 95) 

	# Move the turtle to the ground 
	pen.down() 

	# Set the text color to lightgreen 
	pen.color('lightgreen') 

	# Write the specified text in 
	# specified font style and size 
	pen.write("friendsssss", font=( 
	"Verdana", 16, "bold")) 


# Draw a heart 
heart() 

# Write text 
txt() 

# To hide turtle 
pen.ht()'''