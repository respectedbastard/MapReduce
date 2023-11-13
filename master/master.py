import sys
import requests

links = sys.argv #Получение ссылок из консоли

def distribution_links(links):
    links = links[1:] #Срез имени файла
    #Деление ссылок примерно поровну между slave`ами
    slave1_links = links[:int(len(links) / 2)]
    slave2_links = links[int(len(links) / 2):]
    #Создание словаря, в качестве значения список ссылок
    slave1_links_dict = {"links": slave1_links}
    slave2_links_dict = {"links": slave2_links}

    return slave1_links_dict, slave2_links_dict

def get_results(slave1_links, slave2_links):
    #Отпраление post запроса на slave`ов, передача ссылок в json
    response1 = requests.post('http://localhost:9000/process', json=slave1_links)
    response2 = requests.post('http://localhost:8000/process', json=slave2_links)
    #Получение словарей с подсчитаннми словами
    response1 = response1.json()
    response2 = response2.json()
    #Объединение полученных словарей
    for word, count in response2.items(): #Перебор элементов словаря 2
        if word in response1: #Проверка наличия элемента словаря 2 в словаре 1
            response1[word] += count #Если элемент найден, происходит суммирование значений
        else:
            response1[word] = count #Иначе, добавление элемента в словарь 2
    sorting_result = dict(sorted(response1.items(), key=lambda x: x[1], reverse=True)) #Сорировка нового соловаря по возрастанию значений
    result = dict(list(sorting_result.items())[:10]) #Срез первых 10 элементов словаря
    print(result)


if __name__ == "__main__":
    get_results(*distribution_links(links))