# Дан файл с данными клиентов. Необходимо извлечь все почтовые адреса в отдельный список.
# Для решения задачи необходимо составить регулярное выражение и использовать модуль re.
#
# Примечание. Допустимые доменные зоны - .ru, .com
#
# Пример входных данных:
# Иван ivan228@mail.ru Алексей alexdarkstalker98@gmail.com Петр thegreat@yandex.ru Руслан cheremsha@yahoo.com
#
# Пример выходных данных:
# ivan228@mail.ru
# alexdarkstalker98@gmail.com
# thegreat@yandex.ru
# cheremsha@yahoo.com
from re import finditer
from timeit import timeit

with open(r"files/task-email.txt",encoding="utf-8") as f:
    data=f.readline()

pattern=r"\w+@\w+\.(com|ru)"

matches=[match.group() for match in finditer(pattern,data)]

# print("\n".join(matches))
print(*matches,sep="\n")

