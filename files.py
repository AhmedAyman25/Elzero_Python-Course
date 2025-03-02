import os
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print('*'*30)

# myfile = open(r"H:\Learn_Python\Ahmed.txt",'r')
# print(myfile) # file data object not the content of the file
# print(myfile.mode)
# print(myfile.name)
# print(myfile.encoding)

# print(myfile.read(5)) # read first 5 chars only
# print(myfile.read()) # read all content 
# print(myfile.read(-1)) # read all content 

# print(myfile.readline()) # read 1st line
# print(myfile.readline()) # read 2nd line

# print(myfile.readlines()) # return content of the file in a list
# print(type(myfile.readlines())) # <class 'list'>

# for line in myfile:

#     print(line)

# myfile.close()

# file2 = open(r"H:\Learn_Python\test.txt",'w')
# file2.write("Hi I am Ahmed\n"*5)
# file2.writelines(['Omar\n','Mohammed\n','Ali\n'])
# file2.close()

# file3 = open(r"H:\Learn_Python\test.txt",'a')
# file3.write("this is appended text\n")
# file3.write("another text\n")
# file3.close()

# file4 = open(r"H:\Learn_Python\test.txt",'a')
# file4.truncate(10) # Truncate file to size bytes
# print(file4.tell()) # return cursor position

file5 = open(r"H:\Learn_Python\test.txt",'r')
file5.seek(3) #Set the cursor position, and return the new cursor position.
print(file5.read())

# Remove a file
# os.remove("H:\Learn_Python\test.txt")