import re

def count_words_and_sentences(file_path):
    """
    Зчитує текстовий файл та підраховує кількість слів і речень.

    :param file_path: Шлях до файлу
    :return: Кількість слів і речень у файлі
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        words = re.findall(r'\b\w+\b', text)
        sentences = re.split(r'[.!?…]+', text)

        num_words = len(words)
        num_sentences = sum(1 for s in sentences if s.strip())

        return num_words, num_sentences

    except FileNotFoundError:
        print("Файл не знайдено!")
        return None, None
