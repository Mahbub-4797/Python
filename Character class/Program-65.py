

import re

# pattern = r"[aeiou]"

pattern = r"[A-Z]"
pattern = r"[0-9]"
pattern = r"[A-Z][a-z][0-9]"

# if re.match(pattern,"animal"):
# if re.match(pattern,"Animal"):
# if re.match(pattern,"9Animal"):
if re.match(pattern,"Az9imal"):
    print("Matched")