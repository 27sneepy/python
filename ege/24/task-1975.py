from re import finditer
with open("../../files/24_1975.txt")as f:
    data=f.readline()
pattern=r"[^P]*(P[^P]+)+P[^P]*"

matches=[match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len))) #lambda x: len(x)
