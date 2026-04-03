import re
pattern = r"Colour"

'''
# if re.match(pattern,"Red is a color, I love red colour"):
if re.match(pattern,"Colour is a color, I love red colour"):
    print("Match")
else:
    print("Not Matched")

'''




'''
pattern = r"colour"

print(re.findall(pattern,"Red is a colour, I love red colour"))
'''






pattern = r"colour"
text = "My favourite colour is Red."
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())