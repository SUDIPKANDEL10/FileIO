# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. it take two argument the name of the file and the mode in which the file should be opened. THe mode can be 'r' for reading 'w' for writing and 'a' for appending. text(t), create(x) and binary(b)

f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()