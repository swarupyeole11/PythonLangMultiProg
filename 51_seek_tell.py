#  using the seek function to move curser 5 bytes ahead and then reading the next 10 bytes
# tell : it is used to get postion of current pointer in byres
with open("51_file.txt","r") as file :
    file.seek(5)
    data = file.read(10)
    print(data)

    print(file.tell())

