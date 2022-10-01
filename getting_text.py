import os

def get_txt():
    if not os.path.exists('test.txt'): # если нет (os.path.exists)-возвращает тру если path указывает на
        #существующий путь
        with open('test.txt', 'w', encoding= 'utf-8'):
            pass

    with open('test.txt', 'r', encoding= 'utf-8') as f:
        text = f.read()
        print(f'Содержание файла:\n{text}\nКонец\n')

    txt = input('введите текст: ')
    with open('test.txt', 'w', encoding= 'utf-8') as f:
        f.write(txt +'\n')        

get_txt()        