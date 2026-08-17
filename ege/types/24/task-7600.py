from re import finditer

with open("../../../files/24_7600.txt") as f:
    data=f.readline()


pattern = r"[^QRS]*[QRS][^QRS]*[^QRS]*"

matches=[match.group() for match in finditer(pattern,data)]

print(len(max(matches, key = len)))