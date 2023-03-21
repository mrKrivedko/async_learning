import requests

r: requests.Response = requests.get('https://ya.ru')
# Веб-запрос ограничен производительностью ввода-вывода.

items = r.headers.items()

headers = [f'{key}: {header}' for key, header in items]
# Обработка ответа ограничена быстродействием процессора.

formatted_headers = '\n'.join(headers)
# Конкантенация строк ограничена быстродействием процессора.

with open('headers.txt', 'w') as file:
    file.write(formatted_headers)
    # Запись на диск ограничена производительностью ввода-вывода.
