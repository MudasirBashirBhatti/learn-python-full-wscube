file_path = "C:\\Users\\user\\Desktop\\learn-python-full-wscube\\3. coding start\\12_file_handling\\data.txt"

# update content in file
with open(file_path,"w") as file:
    file.write("update content")

# append content in file
with open(file_path,"a") as file:
    file.write("\nappend content")


# read content in file
with open(file_path,"r") as file:
    content = file.read()
    print(content)

# read content in file line by line
with open(file_path,"r") as file:
    for line in file:
        print(line)

# read content in file line by line and store in list
with open(file_path,"r") as file:
    lines = file.readlines()
    print(lines)

# read content in file line by line and store in list without newline character
with open(file_path,"r") as file:
    lines = [line.strip() for line in file.readlines()]
    print(lines)

# "w" ==> write mode (overwrite existing content)
# "a" ==> append mode (add new content to existing content)
# "r" ==> read mode (read content from file)
# "x" ==> create mode (create a new file, if file already exists then it will raise an error)
# "b" ==> binary mode (used for binary files like images, videos, etc.)
# "t" ==> text mode (used for text files, this is the default mode)
# "r+" ==> read and write mode (read and write content in file)
# "w+" ==> write and read mode (write and read content in file, if file already exists then it will overwrite existing content)
# "a+" ==> append and read mode (append and read content in file, if file already exists then it will add new content to existing content)
# "x+" ==> create and read mode (create a new file and read content from file, if file already exists then it will raise an error)
# "t" and "b" modes can be used in combination with other modes like "r", "w", "a", "x" to specify the type of file (text or binary) being handled. For example, "rt" for reading a text file, "wb" for writing a binary file, etc.
