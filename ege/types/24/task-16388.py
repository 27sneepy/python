from re import finditer

with open("../../../files/24_16388.txt") as f:
    data=f.readline()

# KLMN
# группа может быть неполной
# посл сод не менее 1 полной группы
# MNKLMNKLMNK

# data="MNKLMNKLMNK"

pattern = r"(LMN|MN|N)?(KLMN)+(KLM|KL|K)?"

matches=[match.group() for match in finditer(pattern,data)]

print(len(max(matches, key = len)))