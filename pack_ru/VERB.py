import pymorphy2
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

parts_of_speech_grammems = {  # словарь с обозначениями частей речи и их человеческими названиями
    "VERB": "глагол (личная форма)",
    "INFN": "глагол (инфинитив)",
}

def detect_parts_of_speech(filename, part_of_speech):
    morph = pymorphy2.MorphAnalyzer()
    fin = open(filename, 'r', encoding = 'utf-8')
    text = fin.readlines()
    an_text = []
    for line in text:
        string = ''
        line = line.split()
        for word in line:
            isPoint = False
            if word[len(word)-1] == '.':
                isPoint = True
                word = word.strip('.')
            a = morph.parse(word)
            if a[0][1].POS == part_of_speech:
                word = word.upper()
                word += '<<<<'
                if isPoint == True:
                    word = word + '.'
                string = string + '>>>>' + word + ' '
            else:
                if isPoint == True:
                    word = word + '.'
                string = string + word + ' '
        string = string + '\n'
        an_text.append(string)
    fin.close()
    fout = open('outbuf.txt', 'w', encoding = 'utf-8')
    for line in an_text:
        fout.write(line)
    fout.close()


def main():
    filename_is_incorrect = True
    print("Введите название текстового файла без расширения.\nЧтобы выйти из программы, оставьте строку пустой и нажмите клавишу Enter")
    while filename_is_incorrect:
        try:
            inpname = input()  # считывание ввода 
            if inpname == '':  # если пустой ввод, выходим
                return
            filename = inpname + ".txt"
            fin = open(filename, 'r', encoding = 'utf-8')  # пытаемся открыть файл
            filename_is_incorrect = False  # меняем вспомогательную переменную, чтобы выйти из цикла
        except FileNotFoundError:  # если не получилось открыть файл, выводим сообщение об ошибке
            print(f'Файл "{filename}" не найден. Введите корректное название файла.\nЧтобы выйти из программы, оставьте строку пустой и нажмите клавишу Enter')
    fin.close()  # закрываем файл, потому что функция принимает имя файла (чтобы ее можно было вызывать и из других программ)

    pos_is_incorrect = True
    print("Введите номер части речи, которую необходимо найти.\nЧтобы выйти из программы, оставьте строку пустой и нажмите клавишу Enter")
    grammems = list(parts_of_speech_grammems.keys())  # получаем список обозначений частей речи из словаря
    for i, key in enumerate(grammems):
        print(f"{i + 1} - {parts_of_speech_grammems[key]}")  # выводим человеческие названия частей речи для пользователя
    while pos_is_incorrect:
        try:
            inp_index = input()  # считывание ввода 
            if inp_index == '':  # если пустой ввод, выходим
                return
            pos_index = int(inp_index)  # пытаемся превратить ввод в число
            if pos_index < 1 or pos_index > len(grammems):  # если введено число за границами массива
                print(f'Вы ввели число за пределами диапазона. Введите номер части речи от 1 до {len(grammems)}.\nЧтобы выйти из программы, оставьте строку пустой и нажмите клавишу Enter')
            else:
                pos_is_incorrect = False  # меняем вспомогательную переменную, чтобы выйти из цикла
        except ValueError:  # если не удалось преобразовать ввод в число
            print(f'Вы ввели не число. Введите номер части речи от 1 до {len(grammems)}.\nЧтобы выйти из программы, оставьте строку пустой и нажмите клавишу Enter')

    part_of_speech = grammems[pos_index - 1]  # получаем обозначение части речи по индексу, введенному пользователем
    detect_parts_of_speech(filename, part_of_speech)  # вызываем основную функцию

if __name__ == "__main__":
    main()



