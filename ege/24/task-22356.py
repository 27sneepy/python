from re import finditer

with open("../../files/24_22356.txt") as f:
    data=f.readline()
# 0-9
# A-Z
# макс нечетное 12 ричное
# индекс первого символа в ответе

pattern = r"[1-9AB][0-9AB]*[13579B]"

matches=[match.group() for match in finditer(pattern,data)]

ans=(max(matches,key=lambda x: int(x,12)))
print(data.find(ans))