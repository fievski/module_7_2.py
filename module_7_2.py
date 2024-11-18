from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    str_num = 0
    str_start_byte = file.seek(0)
    for string_ in strings:
        file.write(string_ + '\n')
        str_num += 1
        key = (str_num, str_start_byte)
        string_positions[key] = string_
        str_start_byte = file.tell()
    file.close()
    return string_positions

file_name = 'test.txt'
strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write(file_name, strings)
pprint(result)




# from pprint import pprint

# name = 'test.txt'
# file = open(name, 'r', encoding='utf-8')
# print(file.writable())
# print(file.readable())
# print(file.seekable())
# print(file.tell())
# pprint(file.read())
# print(file.tell())
# file.close()



