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


valid_words = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Words')
unknown_words = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Unnown_Words')
bad_words = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Not_Words')
diff_words = read_lines_from_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Different_Language')

from utils import dictionary_maker

messages = dictionary_maker.get_messages()

for message in messages:
    for word in message.split():
        if word not in valid_words and word not in unknown_words and word not in bad_words and word not in diff_words:
            print(word)
            inp = input('1: Valid, 2: Unknown, 3: Bad, 4: Different\n')

            if inp == '1':
                valid_words.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Words', word)
            elif inp == '2':
                unknown_words.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Unnown_Words', word)
            elif inp == '3':
                bad_words.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Not_Words', word)
            elif inp == '4':
                diff_words.append(word)
                append_line_to_file('C:/Users/Pinki/PycharmProjects/Chat_Bot/data/Different_Language', word)


print('xd')

















