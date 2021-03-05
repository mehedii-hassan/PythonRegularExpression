import re

pattern = r"colo.r"
if re.match(pattern, "colour"):
    print("matched")

pattern = r"^colo..r$"
if re.match(pattern, "colourr"):
    print("matched")

pattern = r"a*"#0 or more
if re.match(pattern, "aaa"):
    print("matched")

pattern = r"a+"#1 or more
if re.match(pattern, "aaa"):
    print("matched")

pattern = r"ice(-)?cream"#0 or 1
if re.match(pattern, "icecream"):
    print("matchedIcecream")