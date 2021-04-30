# Given the names and grades for each student in a class of N students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


n= int(input())
res= []
grade = []
for i in range(n):
  name= input()
  mark= float(input())
  res.append([name,mark])
  grade.append(mark)      # Calculation of second lowest grade
print(res)
print(grade)
grade= sorted(set(grade)) # sorted unique element
print(grade)
m = grade[1]              # gives us second lowest grade
print(m)
name=[]
for val in res:
  if (m==val[1]):
    name.append(val[0])
print(name)               # unsorted
name.sort()
print(name)               # sorted
for nm in name:
  print(nm)