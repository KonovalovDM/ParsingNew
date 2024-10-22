from bs4 import BeautifulSoup
import requests
from googletrans import Translator


# Создаем функцию, которая будет получать информацию с сайта
def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен

        # Создаем объект Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find('div', id='random_word').text.strip()
        # Получаем описание слова
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        # Чтобы программа возвращала словарь
        return {'word': english_words, 'definition': word_definition}
    except Exception as e:
        print('Произошла ошибка:', e)
        return None

# Создаем функцию, которая будет делать саму игру
def word_game():
    translator = Translator()   # Создаем объект переводчика
    print('Добро пожаловать в игру "Слова"')
    while True:
        # Создаем функцию, что бы использовать результаты функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            print('Не удалось получить слово. Попробуйте позже.')
            break

        word = word_dict.get('word')
        definition = word_dict.get('definition')

        # Переводим слово на русский
        translation_definition = translator.translate(definition, src='en', dest='ru').text
        translation_word = translator.translate(word, src='en', dest='ru').text

        # Начинаем игру
        print(f'Описание слова: \n{definition}')
        print(f'Перевод: \n{translation_definition}')
        user_answer = input('\nЧто это за слово? Ваш ответ: ')
        if user_answer.lower() == translation_word.lower():
            print('Правильно!')
        else:
            print(f'Неправильно. Правильным словом было:  {translation_word}, \nчто означает:  {word}')

        # Проверяем, хочет ли пользователь сыграть еще раз
        play_again = input('Хотите сыграть еще раз? (y/n) ')
        if play_again.lower() != 'y':
            break

word_game()

