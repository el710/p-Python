from os import system


system("cls")

def custom_write(file_name, strings):
    strings_positions = {}

    _file = open(file_name, 'w', encoding='utf-8')

    for i in range(len(strings)):
        _key = (i + 1, _file.tell())
        _file.write(strings[i] + '\n')
        strings_positions[_key] = strings[i]

    _file.close()
    return strings_positions


if __name__ == "__main__":

    _name = 'test.txt'
    _info = ["Text for tell.",
        "Используйте кодировку utf-8.",
        "Because there are 2 languages!",
        "Спасибо!"
    ]

    result = custom_write(_name, _info)
    for elem in result.items():
        print(elem)