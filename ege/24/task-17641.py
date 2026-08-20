from re import finditer

with open("../../files/24_17641.txt") as f:
    data=f.readline()

# 9203948*0+92384*0
# 98*0*
number = r"(0|[1-9][0-9]*)"
zero_part = rf"({number}\*)*0(\*{number})*"
pattern = rf"{zero_part}(\+{zero_part})*"

matches=[match.group() for match in finditer(pattern,data)]

print(len(max(matches, key = len)))