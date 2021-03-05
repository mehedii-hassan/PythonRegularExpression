import re

pattern = r"[aeiou]"
if re.match(pattern, "adhgja"):
    print("matched")

pattern = r"[A-Z]"
if re.match(pattern, "Adhgja"):
    print("matched")

pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern, "Aa0hgja0"):
    print("matched")