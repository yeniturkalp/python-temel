# -*- coding: utf-8 -*-


studentsSet = {"ahmet" , "ali" , "Erkan"}

print(studentsSet)

for students in     studentsSet:
    print(students)

print("erkan" in studentsSet)

if "ali" in studentsSet:
    print("listede var")
    
studentsSet.add("melis")    
print(studentsSet)

studentsSet.update(["merih","irrem","cansu"])    
print(studentsSet)
print(len(studentsSet))    
studentsSet.remove("ali")
print(len(studentsSet))
studentsSet.discard("ali")
studentsSet.pop()
studentsSet.clear()
print(type(studentsSet))


print(len(studentsSet))
print(studentsSet)
