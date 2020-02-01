people =  ["joHn","marY", "dANI"]

correct_name = []
for person in people:
    correct_name.append(person.lower())

mylist = [person.title() for person in correct_name]
print(mylist)