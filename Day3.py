#Find the Largest Number in a List
'''
numbers=[10,20,30,40,50]
largest=numbers[3]
#largest= 40

for n in numbers:
    if n>largest:
        largest=n
        print("largest",largest)
#print("The largest number is: "+ str(largest))
'''


#Sum of digits in a number
'''
num=[10,20,30,40,50]
total=0
for n in num:
    total=total + n
    #total+=num
print("The sum of digits in a number is: ", str(total))
'''


#Even numbers count in a list
'''num=[1,2,3,4,5,6,7,8,9,10]
count =0
for n in num:
    if n%2==0:
        count+=1
print("The count of even numbers in a list is: ", str(count))
'''


#list of marks
'''
marks=[50,60,70,80,90]

largest = marks[2]
print("Marks greater than 70 :")
for m in marks:
    if m>70:
        print(str(m))
'''


#nested loops
'''
for i in range(3):
    for j in range(2):
        print(i,j)
'''


#Square Pattern Printing
'''
for i in range(4):
    for j in range(4):
        print("*",end ="")
    print()
'''


#Right Angled Triangle Pattern
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''

#Multiplication Table Pattern
'''
for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()
'''


#Printing Pairs from a List
'''
num=[1,2,3]
for i in num:
    for j in num:
        #print(i,j)
        print(i,j,end=" ")
    print()
'''

#Inverted Right Angled Triangle Pattern
'''
rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
'''


#Functions
'''
def greet():
    print("Hello")

greet()
'''

#Function Ex.
'''
def greet(name):
    print("Hello",name)
greet("Anil")
greet("Suresh")
'''


#Function with Return Value
'''
def add(a,b):
    return a+b
result=add(-1,2)
print("Sum = ",result)
'''


#Even or Odd Function
'''
def check_even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
number=int(input("Enter a Number: "))
print(check_even_odd(number))
'''