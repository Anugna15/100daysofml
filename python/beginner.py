#print statements
print("Hello, World!")
name='John'
age=30
print(name)
print(age)
print("Hello, " + name + "! You are " + str(age) + " years old.")
print("1","2","3",sep=",")
file=open("test.txt","w")
file.write("Hello, World!")
file.close()
#input statements
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Hello, " + name + "! You are " + age + " years old.")
#math operations
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
res=abs(a-b)
print(res)
print(pow(a,b))
print(round(2.5))
#Write a program that prompts the user for two numbers and displays the addition, subtraction, multiplication, and division between them.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Addition: ", num1+num2)
print("Subtraction: ", num1-num2)
print("Multiplication: ", num1*num2)
print("Division: ", num1/num2)
#Write a program that calculates the arithmetic mean of two numbers
mean=(num1+num2)/2
print("Arithmetic mean: ", mean)
#Write a program that calculates the area of a circle from the radius, using the formula A = πr²
import math
radius=float(input("Enter radius: "))
area=math.pi*radius**2
print("Area of circle: ", area)
#Write a program that calculates the area of a triangle from the base and height, using the formula A = 1/2 * base * height
base=float(input("Enter base: "))
height=float(input("Enter height: "))
area=0.5*base*height
print("Area of triangle: ", area)
#Write a program that calculates the delta of a quadratic equation (Δ = b² - 4ac).
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
delta=b**2-4*a*c
print("Delta: ", delta)
#conditionals
num=int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
#comparisons
a=10
b=20
print(a==b)#a is equal to b
print(a!=b)#a is not equal to b
print(a>b)#a is greater than b
print(a<b)#a is less than b
print(a>=b)#a is greater than or equal to b
print(a<=b)#a is less than or equal to b
#logical operators
a=True
b=False
print(a and b)#a and b
print(a or b)#a or b
print(a is b)#a is b
print(not a)#not a


