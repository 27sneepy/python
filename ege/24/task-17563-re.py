from re import *

with open("files/24_17563.txt") as f:
    data = f.readline()

number = r"[789][07-9]*"
pattern=rf"{number}[*-]{number}([*-]{number})*"

matches=[match.group() for match in finditer(pattern,data)]

print(matches)
