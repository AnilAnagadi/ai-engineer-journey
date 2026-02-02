#Calucaltor of sum and product of two numbers
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum=a+b
multiply=a*b
print("Sum of 2 numbers " +str(a)+ " & " +str(b)+ " is " +str(sum)+".")
print("Product of 2 numbers " +str(a)+ " & " +str(b)+ " is " +str(multiply)+".")
'''

#Even or Odd
'''
num = int(input("Enter a Number:   "))
if (num %2)==0:
    print("The number is Even.")
else:
    print("the number is Odd.")
'''

#Forloop
'''
print("No. is less than 4: ")
for i in range(1,11):
  if(i<4):
    print(str(i))
    '''

#Sum of n natural numbers
'''
n = int(input("Enter number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)
'''

#Multiplication table
'''
num = int(input("Enter the Number: "))
for i in range(1,11):
    print(str(num)+" x "+str(i)+" = "+str(num*i))
'''

#Factorial of a number
'''
n=int(input("Enter a Number \n"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of a "+str(n)+" is "+str(fact))    
'''

#Check Prime Number
'''
n=int(input("Enter a Number: "))
is_prime=True

if n<1:
    print("Enter a valid number")
else:
    for i in range (2,n):
        if(n%i==0):
            is_prime=False
            break

if is_prime:
    print(str(n)+" is prime number")
else:
    print(str(n)+" is not prime number")
'''


#Login
'''username= "admin"
password="pass123"

Username = input("Enter your username: ")
Password = input("Enter your password: ")

if(Username==username and Password==password):
    print("Login Successful!")
else:
    print("Login Failed! Try Again.")
'''


#Function to greet user
'''
def greet(name):
    print("Hello", name)
greet("Anil")
'''


#Function to calculate area of circle
'''
def area_of_circle(radius):
    area=3.14*radius*radius
    return area
r=int(input("Enter radius of circle:"))
result=area_of_circle(r)
print("Area of circle with radius "+str(r)+" is "+str(result))
'''


#fibonacci series
'''
n=int(input("Enter number of terms: "))
a=0
b=1
print("Fibonacci Series: ")
for i in range (n):
    print(a)
    c=a+b
    a=b
    b=c'''

#reverse a string
'''
1
str=input("Enter a String")
reversed_str=""
for char in str:
    reversed_str=char+reversed_str
print("Reversed String is: "+reversed_str)

2
text = input("Enter a String: ")
print("Reversed String is:", text[::-1])
'''


#palindrome check
'''
str=input("Enter a String: ")
reversed_str=str[::-1]
if str==reversed_str:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")
'''

'''
name = input("enter ur name")
age=int(input("enter ur age"))
print("hello "+name+ "next year u will be turning to "+str(age+1))
'''
#f-string (Formatted string) 
#The f before the quotes tells Python: “Evaluate whatever is inside {} and insert the result here.”
'''
print(f"hello {name} next year u will be turning to {age + 1}")
'''



name = input("Enter your name: ")
year = int(input("Enter current year: "))

print("Hello", name)
print("In 2030, your experience as a developer will be:", 2030 - year, "years")
