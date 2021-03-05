import re

pattern = r"colour"
if re.match(pattern, "Red is a colour,I love red color"):
    print("Match")
else:
    print("Not Matched")

if re.search(pattern, "Red is a colour,I love red color"):
    print("Match")
else:
    print("Not Matched")

print(re.findall(pattern, "Red is a colour,I love red colour"))
