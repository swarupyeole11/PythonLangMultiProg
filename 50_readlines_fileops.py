#  write code to read marks of the students 3 students seprated by newliens and give avg of their 3 scores seprated by commas

# Method1 
#  code to calculate percetnage marks of each stundent in the student_marks file
with open("student_marks.txt","r+") as file :
     
  marks_line = file.readlines()
  student_count  = 0
  print(marks_line)
  
  #reading eachline in the marks line list 
  for line in marks_line :
     
    if(line != "\n"):
      
      student_count = student_count + 1
      marks1 = float(line.split(",")[0])
      marks2 = float(line.split(",")[1])
      marks3 = float(line.split(",")[2])
      percentage = ((marks1+marks2+marks3)/300)*100

      print("The Percentage marks of student ", student_count ,"is :" , percentage, "\n" )


# Method2
#  code to calculate percetnage marks of each stundent in the student_marks file
with open("student_marks.txt","r") as file :
   
   student_cnt = 0

   while True :
      student_cnt+=1
      line = file.readline()

      if not line:
         break
      
      marks1a = float(line.split(",")[0])
      marks2a = float(line.split(",")[1])
      marks3a = float(line.split(",")[2])
      percentage = ((marks1a+marks2a+marks3a)/300)*100

      print("The Percentage marks of student ", student_cnt ," using method2 is :" , percentage )



#  code to write into the file with a line break 

mylines = ["94,95,93", "98,98,97", "89,98,79"]

with open("student_marks.txt","a") as file:
    for line in mylines:
       file.write(line + '\n')
