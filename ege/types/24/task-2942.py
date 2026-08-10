from re import *
with open(r"../../../files/24_2942.txt") as f:
    data = f.readline()

pattern=r"(A[CB])+"

matches=[match.group() for match in finditer(pattern,data)]

print(len(max(matches, key = len))//2)


