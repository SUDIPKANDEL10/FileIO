# readlines()method

# the readline() method reads a single line from the file. If we want to read multiple lines, we ca use a loop.
# THe readlines() method reads all the lines of the file and returns them as a  list of string.

# f = open ('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)



    # writelines() method
    # the writelines() method in Python writes a sequence of strings to a file. The Sequence can be any iterable objects. such as a list or a tupel.
    # This will write the strings inthe lines to the file myfile.txt The \n characters are used to add newline characters to the end of each string.
    # Keep in mind that the writelines() method does not add newline characters between the strings in the sequences if yoy want to add newlines between the strings you can use a loop to write each string separately:
# f = open('myfile2.txt','w')
# lines = ['line1\n', 'line 2\n', 'line3\n']
# f.writelines(lines)
# f.close()

#seek()  and  tell() function 
# in python the seek() and tell() functions are used to work with file objects and their positions within in a file.
# THeses functions are part of the built in IO module, which provides a consistent interface reading and writing to various file-like objects, such as files, pipes and in-memory buffers.

# seek() function

# It allows you to move the current position within a file to specific point. The position is specific in bytes, adn you can move either forwrard or backward fromm the current position 
# for example
# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     f.seek(20)   #move to the 10th byte in the file
#     data = f.read(5)  # Read the next 5 bytes
#     print(data)


#     tell()function Its returns the current position withiin the file, in bytes.
# example 
# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     f.seek(20)   #move to the 10th byte in the file
#     print (f.tell())
#     data = f.read(5)  # Read the next 5 bytes
#     print(data)

# truncate()function  when you open a file in python using the open function you can specify the mode in which you want to open the file if you specify  the mode in 'w' or 'a' the fiel is opened in write mode and you can write to the file. if you want to truncate the file to a specific size, you can use the ktruncate

with open ('sample.txt','w') as f:
    f.write('tara chandra kandel')
    # f.truncate(9)     #o/p tara chan
with open('sample.txt','r') as f:
    print(f.read)
