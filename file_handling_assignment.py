file=open("my_file.txt", "w")
file.write("Hi,this is the first line.\n")
file.write("the 2nd line has:123.\n")
file.write("This is line 3.\n")

file=open("my_file.txt", "r")
contents = file.read()
print("File Contents:")
print(contents)

file=open("my_file.txt", "a")
file.write("appending the first line.\n")
file.write("appendind the 2nd line with numbers:456.\n")
file.write("appending line 3.\n")

try:
    file = open("non_existent_file.txt", "r")
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("Done handling exceptions.")
file.close()