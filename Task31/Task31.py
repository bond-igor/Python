"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

first_key = ['computer', 'printer', 'keyboard', 'mouse']

second_key = 4
third_key = {'computer': '200€-1000€', 'printer': '200€-500€',
             'keyboard': '5€-9€', 'mouse': '4€-7€'}
# создаем словарь
to_yaml = {'items': first_key, 'items_quantity': second_key,
           'items_price': third_key}
#открываем файл для записи в кодировке utf-8
with open('file.yaml', 'w', encoding='utf-8') as t_f:
    # записываем словарь в файл
    yaml.dump(to_yaml, t_f, allow_unicode=True, default_flow_style=False)
# открываем файл для чтения
with open('file.yaml', encoding='utf-8') as file_read:
    # сравниваем данные из файла с исходным словарем
    print(f'Проверка правильности записи данных: '
          f'{yaml.safe_load(file_read) == to_yaml}')
