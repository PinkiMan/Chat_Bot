import os
import json


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


def decode(msg):
    if msg == '\u00c3\u00ad':
        return 'í'
    elif msg == '\u00c4\u009b':
        return 'ě'
    elif msg == '\u00c5\u00af':
        return 'ů'
    elif msg == '\u00c3\u00a9':
        return 'é'
    elif msg == '\u00c3\u00a1':
        return 'á'
    elif msg == '\u00c5\u0099':
        return 'ř'


def check_letter(letter):
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzĚŠČŘŽÝÁÍÉěščřžýáíé0123456789+-*/=;,.?:_!(/úÚůŮ)[]@{}\n "\"\\ďĎ'

    if letter not in Letters:
        return '|?|'
    else:
        return letter



def get_messages():
    file = open('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/message_1.json', 'r', encoding='utf-8')
    exx = file.read()
    new = exx.replace('\\u00c3\\u00ad', 'í')
    new = new.replace('\\u00c4\\u009b','ě')
    new = new.replace('\\u00c5\\u00af','ů')
    new = new.replace('\\u00c3\\u00a9','é')
    new = new.replace('\\u00c3\\u00a1','á')
    new = new.replace('\\u00c5\\u0099','ř')
    new = new.replace('\\u00c5\\u00be','ž')
    new = new.replace('\\u00c4\\u008f','ď')
    new = new.replace('\\u00c4\\u008d','č')
    new = new.replace('\\u00c5\\u00a1','š')
    new = new.replace('\\u00c3\\u00ad','í')
    new = new.replace('\\u00c3\\u00bd', 'ý')
    new = new.replace('\\"','\'')

    datas_text = ''
    for char in split_string_to_chars(new):
        datas_text += check_letter(char)

    datas = json.loads(datas_text)

    messages = []
    for message in datas['messages']:
        if 'content' in message:
            content = message['content']
            messages.append(content)

    return messages



print('Xd')








