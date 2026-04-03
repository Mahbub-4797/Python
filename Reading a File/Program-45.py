



file = open("C:\\E - Folder\\Software Engineering\\Python\\Reading a File\\student.txt","r+")

# text = file.read()
# print(text)

'''
size = len(text)
print(size)
'''

'''
text = file.readlines()

print(text)

'''


for line in file:
    print(line)


file.close()