
'''

# 1 + 2 + 3 + ... + n

n = int(input("Enter the last number : "))

sum = 0
for x in range(1,n+1,1):
    sum = sum + x
print(sum)





# 2 + 4 + 6 + ... + n

n = int(input("Enter the last number : "))

sum = 0
for x in range(2,n+1,2):
    sum = sum + x
print(sum)





# 1 + 3 + 5 + ... + n

n = int(input("Enter the last number : "))

sum = 0
for x in range(1,n+1,2):
    sum = sum + x
print(sum)






# 4 + 8 + 12 + ... + n

n = int(input("Enter the last number : "))

sum = 0
for x in range(4,n+1,4):
    sum = sum + x
print(sum)

'''



'''

# 1**2 + 2**2 + 3**2 + ... + n**2

n = int(input("Enter the last number : "))

sum = 1
for x in range(1,n+1):
    sum = sum + x**2
print(sum-1)

'''



'''

# 2**2 + 4**2 + 6**2 + ... + n**2

n = int(input("Enter the value of n : "))

sum = 1

for x in range(2,n+1,2):
    sum = sum + x**2
print(sum-1)

'''






# 1 + 1/2 + 1/3 + ... + 1/n

n = int(input("Enter the value of n : "))

sum = 0

for x in range(1,n+1,1):
    sum = sum + 1/x
print(sum)
