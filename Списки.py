'''
ПЕРЕБОР ЭЛЕМЕНТОВ
people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

while i < len(people)
   print(people[i])
   i = i + 1
'''
'''
ОБРАЩЕНИЕ К ЭЛЕМЕНТАМ СПИСКОВ

people = ["Tom", "Sam", "Bob"]
one, two, three = people
print(two) # ----> Sam

people = ["Tom", "Sam", "Bob"]
# получение элементов с начала списка
print(people[0])   # Tom
print(people[1])   # Sam
print(people[2])   # Bob
 
# получение элементов с конца списка
print(people[-2])   # Sam
print(people[-1])   # Bob
print(people[-3])   # Tom
'''
'''
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
first_three_peoples = people[:3]
from_three_to_five = people[0:2]
print(first_three_peoples)
print(from_three_to_five)
'''
people = ["Ivan", "Stepan", "Rosa", "Sam", "Bob", "John", "Jeson"]
ivan_and_other_two = people[0:7:2] #------> (Ivan, Rosa, Bob, Jeson)
print(ivan_and_other_two)