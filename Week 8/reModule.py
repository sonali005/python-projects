import re

for match in re.findall("\d[a-z]", "1ab23c"):
    print(match)