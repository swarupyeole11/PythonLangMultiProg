# this is the python way of anonymus functions 

# the syntax is ->   lambda arguments: expression


# here we are passsing the fucniton as a paremter : the logic is whenever fx is called then
#  it should behave like the function desc provided to it

def numberplus6(fx,num):
    return 6+fx(num)

finalnum = numberplus6(lambda x : x*x, 2)

print(finalnum)

############################################################################################################################################################
#You can also store the function in a variable
cubeandmutiply = lambda x,y : x*x*x*y
print(cubeandmutiply(2,3))



############################################################################################################################################################
#Q  Write a Python program to sort a list of dictionaries using Lambda on the basis of color
dicty = [{'make': 'Nokia', 'model': 216, 'color': {'supercolor':'Black'}}, {'make': 'Mi Max', 'model': '2', 'color':  {'supercolor':'Gold'}}, {'make': 'Samsung', 'model': 7, 'color':  {'supercolor':'Blue'}}]
#  here the x refers to each of the each element in the iterable which here is the list and the 
ordered = sorted(dicty, key = lambda x : x['color']['supercolor'])
print(ordered)


############################################################################################################################################################
#Q  Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.

n = int(input("Enter number of students : "))

def studentinput():
    listofstudents = []
    for _ in range(n):
     name = input("Enter the name : ")
     grades = input("Enter the grades : ")
     listofstudents.append([name,int(grades)])
    return listofstudents

def orderedlist_of_students(listofstudents):
    return sorted(listofstudents, key = lambda x : int(x[1])) 

listofstudents = studentinput()
print(orderedlist_of_students(listofstudents))












    



