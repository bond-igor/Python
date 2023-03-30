"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

def type_check(list):
    for word in list:
        enc_word = word.encode('utf-8')
        print(f'"{word}" в виде байтов: {enc_word}')
        print(f'Тип: {type(enc_word)}')
        dec_word = enc_word.decode('utf-8')
        print(f'{enc_word} в строковом виде: {dec_word}')
        print(f'Тип: {type(dec_word)}')

type_check(['разработка', "администрирование", "protocol", 'standard'])
