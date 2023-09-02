import os
import sys

BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    chars_stop = [',', '.', '!', ':', ';', '?']
    end = start + size
    if end + 1 > len(text):
        part_text = text[start:]
        return (part_text, len(part_text))
    if text[end] in chars_stop:
        while text[end - 1] in chars_stop:
            end -= 1
    while text[end - 1] not in chars_stop:
        end -= 1

    part_text = text[start:end]
    return (part_text, len(part_text))


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path) as file_txt:
        text = ''.join(file_txt.readlines()).lstrip()
    start = 0
    num_page = 1
    while start < len(text):
        part_text = _get_part_text(text, start, PAGE_SIZE)
        book[num_page] = part_text[0].lstrip()
        start += part_text[1]
        num_page += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
