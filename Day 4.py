#Dictionaries
student = {
    "name": "John",
    "age": 21,
    "courses": "AI"
}
'''
print(student)
student["city"] = "Bangalore"
print(student["age"])
print(student["city"])
for key in student:
    print(key)

for key, value in student.items():
    print(key, ":", value)
'''



#Dictionary Example with Keys and Values
'''
student = {
    "name": "Anil",
    "marks": 85,
    "grade": "A"
}

for k, v in student.items():
    #print(k, ":", v)
    print(f"{k} : {v}")
'''

#Count frequency of characters in a string
'''
word = "banana"
count = {}
for char in word:
    if char in count:
        count [char] +=1
    else:
        count [char]=1
for k, v in count.items():
    print(f"{k} : {v}") 
    '''


#Store Multiple Students
'''
students = [
    {"name":"Anil", "marks":85, "grade":"A"},
    {"name":"Binu", "marks":78, "grade":"B"},
    {"name":"Cathy", "marks":92, "grade":"A"}
    ]
for s in students:
    print(s["name"], "scored", s["marks"], "and got grade", s["grade"])
    #print(f"Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")
'''

store = [
    {"brand":"Toyoto", "model":"Camry", "year":2020, "price":25000},
    {"brand":"Honda", "model":"Civic", "year":2019, "price":22000},
    {"brand":"Ford", "model":"Mustang", "year":2021, "price":35000}
]
for car in store:
    #print(car["brand"], car["model"], car["year"], car["price"])
    print(f"Brand: {car['brand']}, Model: {car['model']}, Year: {car['year']}, Price: ${car['price']}")