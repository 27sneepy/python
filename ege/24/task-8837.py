import re

with open(r"Task-24\files\24-371.txt") as f:
    data = f.read()
pattern = r'[A-Z]([A-Z ]*[A-Z])?\.'
matches = [match.group() for match in re.finditer(pattern, data)]

ans = 0
for match in matches:
    if not any(char in match for char in 'XYZ'):
        ans = max(ans, len(match))
    elif len(match) > ans:
        # Вариант решения 1
        r = len(match) - 1
        while match[r] not in 'XYZ':
            r -= 1
        ans = max(ans, len(match[r + 1:].lstrip()))

        # Вариант решения 2
        for i in 'XYZ': match = match.replace(i, '*')
        match = match.split('*')[-1].lstrip()
        ans = max(ans, len(match))

print(ans)