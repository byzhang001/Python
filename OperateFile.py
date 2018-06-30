file=open("data.txt","w")
file.write("Hello world")
file.write("This is a line\n")
txt_lines=[
    "Chapter 3\n",
    "Sample text data file\n",
    "Edit the file with any text editor\n"
]
file.writelines(txt_lines)
file.close()
file=open("data.txt","r")
#char = file.read(10)
#print(char)
#one_line=file.readline()
#print(one_line)
all_data=file.readlines()
print(all_data)
print("Lines:",len(all_data))
for line in all_data:
    print(line.strip())
print(all_data[2])
file.close()