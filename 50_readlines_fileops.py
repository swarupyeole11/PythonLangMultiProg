#  write code to read marks of the students 3 students seprated by newliens and give avg of their 3 scores seprated by commas

#  code to calculate percetnage marks of each stundent in the student_marks file
with open("student_marks.txt","r+") as file :
     
  marks_line = file.readlines()
  student_count  = 0

  for line in marks_line :
     
     student_count = student_count + 1

     marks1 = float(line.split(",")[0])
     marks2 = float(line.split(",")[1])
     marks3 = float(line.split(",")[2])
     percentage = ((marks1+marks2+marks3)/300)*100

     print("The Percentage marks of student ", student_count ,"is :" , percentage )

