"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet
import os

def site_ping(sites):
    for site in sites:
        # команда для подпроцесса
        args = ['ping', site]
        # инициируем создание подроцесса, передаём команду, записываем в
        # переменную результат выполнения
        site_ping=subprocess.Popen(args, stdout=subprocess.PIPE)
        # читаем построчно результат
        for line in site_ping.stdout:
            # определяем кодировку
            encoding_check = chardet.detect(line)
            # декодируем результат используя найденую кодировку
            print(line.decode(encoding_check['encoding']))

site_ping(['yandex.ru', 'youtube.com'])