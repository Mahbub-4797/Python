
# stack

'''
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
# print(books)
print("Now the top book is : ",books[-1])


books.pop()
print("Now the top book is : ",books[-1])

books.pop()
if not books:
    print("No books left")

'''



# Queue

from collections import deque

bank = deque(["Anis", "Karim", "Bijoy"])
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")