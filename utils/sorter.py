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


pravopisne = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/pravopisne_dobre')
chybne = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/slova_s_chybou')
cizi = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/cizi_slova')
nezarazeno = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nezarazeno')
nesmysl = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nesmysl')


from utils import dictionary_maker

messages = dictionary_maker.get_messages()

for message in messages:
    for word in message.split():
        if word not in pravopisne and word not in chybne and word not in cizi and word not in nezarazeno and word not in nesmysl:
            print(word)
            inp = input('1: pravpisne, 2: chybne, 3: cizi, 4: nezarazeno, 5: nesmysl\n')

            if inp == '1' or inp == '':
                pravopisne.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/pravopisne_dobre', word)
            elif inp == '2':
                chybne.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/slova_s_chybou', word)
            elif inp == '3':
                cizi.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/cizi_slova', word)
            elif inp == '4':
                nezarazeno.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nezarazeno', word)
            elif inp == '5':
                nesmysl.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/word/nesmysl', word)


print('xd')

















