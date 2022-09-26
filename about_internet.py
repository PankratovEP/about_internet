from re import *
import requests
first, sec = input(), input()
spisok = findall(r'a href="(http.*)">', requests.get(first).text)
for i in spisok:
    buf = requests.get(i)
    if sec in buf.text:
        exit(print('Yes'))
print('No')

