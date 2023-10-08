# Code to how to read the file
# f = open("myfile.txt","r")
# line = f.read()
# print(line)
# f.close()

# # code to how to append and read a file
# fw = open("myfile.txt","a+")
# fw.write("This is The new appended string")
# x = fw.read()
# fw.close()
# print(x)


#code to avoid the use of f.close
with open("myfile2.txt","x") as file :
    file.write("This is the new file I have created")

