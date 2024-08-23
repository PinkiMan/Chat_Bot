import json
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



def process_file(filename):
    file = open(filename, 'r', encoding='utf-8')
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

    try:
        datas = json.loads(new)
    except:
        return

    messages = []
    for message in datas['messages']:
        if 'content' in message:
            content = message['content']
            messages.append(content)

    all_messages = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/messages')
    with open('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/messages', 'a', encoding='utf-8') as file:
        for message in messages:
            if message not in all_messages:
                all_messages.append(message)
                file.write(message+'\n')


def walk_database():
    directory = 'E:/TrashFolder/Facebook Data-JSON/messages/inbox'
    for chat in os.listdir(directory):
        for item in os.listdir(os.path.join(directory, chat)):
            file = os.path.join(directory, chat, item)
            if os.path.isfile(file):
                process_file(file)
                print(f'Chat {chat} processed')






#process_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/message_1.json')
print('Xd')





