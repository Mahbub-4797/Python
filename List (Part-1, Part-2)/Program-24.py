

subjects = ["C", "C++", "Java", "Python", "BASIC"]
subjects.append("TOC")
print(subjects)


subjects.insert(2,"OS")
print(subjects)



subjects.remove("BASIC")
print(subjects)


subjects.sort()
print(subjects)


numbers = [20,4,10,33,15,102,59, 20]
# numbers.sort()
print(numbers)


'''
numbers.reverse()
print(numbers)

numbers.pop()
numbers.pop()
print(numbers)


numbers.clear()
print(numbers)
'''

numbers1 = numbers.copy()
print(numbers1)



pos = numbers.index(15)
print(pos)

x = numbers.count(20)
print(x)