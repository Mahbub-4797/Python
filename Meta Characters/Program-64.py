
import re


'''
pattern = r"colo.r"     # any 1 character
pattern = r"colo..r"     # any 2 character
pattern = r"^colo..r$"     # ^ => must be start with "colo"   and   $ => must be end with 'r'
'''

'''
pattern = r"a*"         # 0 or more
pattern = r"(ab)*"
'''


'''
pattern = r"a+"         # 1 or more
pattern = r"a+"


# if re.match(pattern,"abroad"):
# if re.match(pattern,"coloubr"):
'''

'''
 pattern = r"ice(-)?cream"       # ? => 0 or 1

if re.match(pattern,"ice-cream"):
    print("Matched")

'''


pattern = r"a{1,3}$"            # 1-3   "a"

if re.match(pattern,"aaa"):
    print("Matched")