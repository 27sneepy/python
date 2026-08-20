from re import finditer

with open("../../files/24_23206.txt") as f:
    data=f.readline()
# 0-9
# A-Z
# макс последовательность среди которых 35 букв S
# нач четной цифрой
# не сод других четных цифр кроме первой

# 8******S****S****S***

pattern = r"[02468][^02468S]*(S[^02468S]*){35}"

matches=[match.group() for match in finditer(pattern,data)]

print(len(max(matches, key = len)))