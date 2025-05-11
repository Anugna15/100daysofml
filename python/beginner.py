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

#conditionals
num=int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#Make a program that asks for a person's age and displays whether they are of legal age or not
age=int(input("Enter your age: "))
if age>=18:
    print("You are of legal age.")
else:
    print("You are not of legal age.")
#Make a program that asks for a number and displays whether it is even or odd
num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")
#Write a program that reads two numbers and tells you which one is bigger.
a=int(input("enter a 1st number: "))
b=int(input("enter 2nd number: "))
if a>b:
    print(a,"is bigger than",b)
elif b>a:
    print(b,"is bigger than",a)
else:
    print(a,"is equal to",b)

#Write a program that asks the user for three numbers and displays the largest one
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
if a>b & a>c:
    print(a,"is the largest number")
elif b>a & b>c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")
#Make a program that reads the grades of two tests, calculates the simple arithmetic mean, and informs whether the student passed (average greater than or equal to 6) or failed (average less than 6)
test1=float(input("Enter the grade of the 1st test: "))
test2=float(input("Enter the grade of the 2nd test: "))
average=(test1+test2)/2
if average>=6:
    print("You passed")
else:
    print("You failed")
#Make a program that reads three numbers, and informs if their sum is divisible by 5 or not
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
sum=a+b+c
if sum%5==0:
    print("The sum is divisible by 5")
else:
    print("The sum is not divisible by 5")
#Make a program that asks for two numbers and displays if the first is divisible by the second
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if a%b==0:
    print(a,"is divisible by",b)
else:
    print(a,"is not divisible by",b)
#repeat loops
for i in range(10):
    print(i)
#Make a program that prints the numbers from 1 to 10
for i in range(1,11):
    print(i)
#Make a program that prints the even numbers from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)
#Make a program that prints the odd numbers from 1 to 20
for i in range(1,21):
    if i%2!=0:
        print(i)
#Make a program that prints the multiplication table of a number entered by the user
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
#Make a program that prints the first 10 numbers of the Fibonacci sequence
a=0
b=1
print(a)
print(b)
for i in range(8):
    c=a+b
    print(c)
    a=b
    b=c
#while loops
i=0
while i<10:
    print(i)
    i+=1
#Make a program that prints the numbers from 1 to 10 using a while loop
i=1
while i<=10:
    print(i)
    i+=1
#counting down from 10 to 1
count=0
while count<10:
    print(count)
    count+=1
#Write a program that prints all even numbers from 1 to 100.
count=0
while count<100:
    if count%2==0:
        print(count)
    count+=1
#2nd solution
count=0
while count<100:
    print(count)
    count+=2
#Make a program that prints the multiplication table of a number entered by the user using a while loop
num=int(input("Enter a number: "))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1
#Make a program that prints the first 10 numbers of the Fibonacci sequence using a while loop
n=int(input())
a=0
b=1
print(a)
print(b)
i=2
while i<n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
#Make a program that asks for a number and prints its factorial using a while loop
num=int(input("Enter a number: "))
factorial=1
i=1
while i<=num:
    factorial*=i
    i+=1
print("Factorial of",num,"is",factorial)

#for loop 
fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)
for i in range(5,3,-1):
    print(i)
#Create a program that prompts the user for a number and displays the table of that number using a loop
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
#Create a program that prompts the user for a number and displays the factorial of that number using a loop
num=int(input("Enter a number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("Factorial of",num,"is",factorial)
#Create a program that prompts the user for a number and displays the Fibonacci sequence up to that number using a loop
num=int(input("Enter a number: "))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    print(c)
    a=b
    b=c
#Create a program that prompts the user for a number and displays the sum of all numbers from 1 to that number using a loop
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of all numbers from 1 to",n,"is",sum)
#prime number
n=int(input())
if n<2:
    print(n,"is not prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(n,"is not prime")
            break
    else:
        print(n,"is prime")
#Create a program that displays the first N prime numbers, where N is informed by the user, using a loop
n=int(input("Enter a number: "))
count=0
num=2
while count<n:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            break
    else:
        print(num)
        count+=1
    num+=1
# Create a program that displays the first N first perfect squares, where N is informed by the user, using a loop.
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i**2)
# Write a program that prompts the user for two numbers A and B and displays all numbers between A and B.
a=int(input("Enter A: "))
b=int(input("Enter B: "))
for i in range(a,b+1):
    print(i)
    