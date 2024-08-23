import os


def file_exists(filename: str) -> bool:
    """ does file exist

        :param filename: full directory of file + filename
        :return: True if file exists else False

        Example:
        file_exists(filename: 'file.txt') -> True
    """
    if type(filename) is not str:
        raise TypeError
    else:
        return os.path.isfile(filename)


def split_string_to_chars(string: str) -> list:
    """ returns list of chars in string

        :param string: str for split to characters
        :return: list of characters split from str

        Example:
        split_string_to_chars(string: 'some text') -> ['s', 'o', 'm', 'e', ' ', 't', 'e', 'x', 't']
    """
    if type(string) is not str:
        raise ValueError
    else:
        new_list = []
        for character in string:
            new_list.append(character)
        return new_list


def replace_invalid_letters(string):
    letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzĚŠČŘŽÝÁÍÉěščřžýáíé0123456789+-*/=;,.?:_!(/úÚůŮ)[]@{}\n "\"\\ďĎ'

    new_string = ''

    for letter in split_string_to_chars(string):
        if letter in letter_list:
            new_string += letter
        else:
            new_string += '$'

    return new_string


def append_line_to_file(filename: str, line: str) -> None:
    """ writes string at the end of file if it exists, without overwrites

        :param filename: full directory of file + filename
        :param line: str to write at the end in file, '\\n' will be added
        :return: None

        Example:
        append_line_to_file(filename: 'file.txt', line: 'some text') -> None
    """
    if type(filename) is not str or type(line) is not str:
        raise TypeError
    else:
        if not file_exists(filename):
            raise FileNotFoundError
        else:
            with open(filename, 'a', encoding='utf-8') as FILE:
                FILE.write(line + '\n')


def read_lines_from_file(filename: str) -> list[str]:
    """ read all lines from file

        :param filename: full directory of file + filename
        :return: list of lines from file (str) without '\\n'

        Example:
        read_lines_from_file(filename: 'file.txt') -> ['some text','another text']
    """
    if type(filename) is not str:
        raise TypeError
    else:
        if not file_exists(filename):
            raise FileNotFoundError
        else:
            lines = []
            with open(filename, 'r', encoding='utf-8') as FILE:
                for line in FILE:
                    new_line = line.replace('\n', '')
                    lines.append(new_line)

            return lines


pravopisne = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/pravopisne_dobre')
chybne = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/slova_s_chybou')
cizi = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/cizi_slova')
nezarazeno = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nezarazeno')
nesmysl = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nesmysl')
nespisovne = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nespisovne')


messages = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/messages')
all_words = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/ALL_Words')
for message in messages:
    words = message.split()
    for word in words:
        if word not in all_words:
            all_words.append(word)
            append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/ALL_Words', word)

print('xd')





