'''while True:
    znach=float(input('Задайте коэф.усиления = '))
    if znach<17.5 or znach>23.8:
        print('Ошибка!')
    else:
        break'''

import requests
res = requests.get('https://docs.python.org/3.5/')
print(res.status_code)
print(res.headers['Content-Type'])
print(res.content)
print(res.text)