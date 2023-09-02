# Не удаляйте эти объекты - просто используйте
book: dict[int, str] = {}
PAGE_SIZE = 1050

def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    chars_stop = [',', '.', '!', ':', ';', '?']
    end = start + page_size
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

# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file_txt:
        text = ''.join(file_txt.readlines()).lstrip()
    start = 0
    num_page = 1
    while start < len(text):
        part_text = _get_part_text(text, start, PAGE_SIZE)
        book[num_page] = part_text[0].lstrip()
        start += part_text[1]
        num_page += 1

prepare_book('tmp_book.txt')
print(book[12])
