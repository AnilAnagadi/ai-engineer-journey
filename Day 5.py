#Strings
'''
word="Hello"
#print(word[1])
#print(word[-1]) #last letter
print(word[1:3]) #slicing
'''


#Loops
'''
for i in "word":
    print(i)
'''


#String Methods
'''
text = "HELlo World"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.replace("o", "0"))
print(text.split())
print(text.find("o"))
print(text.count("o"))
print(text.startswith("H"))
print(text.endswith("d"))
print(text.isalpha())
print(text.isdigit())   
print(text.isalnum())
print(text.index("o"))
'''


#reverse a String
'''text="Hello"
reversed_text=text[::-1]
print(reversed_text)
'''



#Vowels Count
'''
text = input("Enter a String : ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count = count+1
print("Number of Vowels in the String is: ", count)
print("the Vowels are: ", end=" ")
for char in text:
    if char in vowels:
        print(char, end=" ")
'''


#palindrome check
word = input("Enter word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
