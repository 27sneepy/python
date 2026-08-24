from re import finditer, sub

with open("../../files/24-371.txt") as f:
    data = f.readline()

pattern = r"([A-Z]+ +)+[A-Z]+\."

matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    l = match[:-1].replace(" ", "*")
    l = sub(r"\*[A-Z]", "* Z", l)
    l = l.split()
    while l != sorted(l, key=lambda x: len(x.strip("*")), reverse=True):
        l = l[1:]
    ans = max(ans, len("".join(l)) + 1)
print(ans)
