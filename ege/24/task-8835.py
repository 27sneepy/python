import re

with open(r'../../files/24-8835.txt') as f:
    data = f.read()

pattern = r'[^.]+\.'
matches = [match.group() for match in re.finditer(pattern, data)]

ans = 0
for match in matches:
    cnt_M = match.count('M')
    if match.count('M') == 112:
        ans = max(ans, len(match))
    elif cnt_M > 112 and len(match) > ans:
        r = len(match) - 1
        new_cnt_M = 0
        while new_cnt_M <= 112:
            if match[r] == 'M': new_cnt_M += 1
            r -= 1
        ans = max(ans, len(match[r + 2:]))

print(ans)