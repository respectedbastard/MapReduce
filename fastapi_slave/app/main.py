from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
from pydantic import BaseModel

app = FastAPI()

main_dict = {}

#Создание модель валидации данных
class Links(BaseModel):
    links: list

#Получение запроса
@app.post("/process")
def count_words(links: Links):
    clear_dict()
    #Получение списка ссылок
    links = links.links
    #Получение количества слов с каждой страницы
    for link in links:
        #Запрос страницы
        response = requests.get(link)
        #Парсинг страницы
        page = BeautifulSoup(response.content, 'html.parser')
        #Получение текта страницы
        text = TextBlob(page.get_text())
        text = text.lower()
        #Получение словаря посдчитанных слов
        words_counter = text.word_counts
        #Сортировка словаря по убыванию значений
        words_counter = dict(sorted(words_counter.items(), key=lambda x: x[1], reverse=True>
        #Объединение всех получаемых словарей
        for word, count in words_counter.items(): #Перебор элементов словаря words_counter
            if word in main_dict: #Проверка наличия элемента словаря words_counter в словар>
                main_dict[word] += count #Если элемент найден, происходит суммирование знач>
            else:
                main_dict[word] = count  #Иначе, добавление элемента в словарь main_dict
    return main_dict

def clear_dict():
    main_dict.clear()