

# xargs 

'''
def student (*deatils):
    print(deatils)


student(101, "Anis")
student(101, "Anis", 3.75)

'''

'''

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


add(10,20)
add(10,20,30,40,50)

'''




# xxargs

def student (**details):
    print(details)
    print(details["name"])


student(id=101,name="Anis")