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
f = open('myfile2.txt','w')
lines = ['line1\n', 'line 2\n', 'line3\n']
f.writelines(lines)
f.close()
