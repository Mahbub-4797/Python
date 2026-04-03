
# sub(pattern,replace,string)

import re

pattern = r"colour"
text1 = "My favourite colour is Red. I love blue colour as well."
text2 = re.sub(pattern,"color",text1,count=2)
print(text2)