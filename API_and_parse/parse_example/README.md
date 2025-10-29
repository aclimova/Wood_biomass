# Парсер Rick and Morty API JSON

Данный скрипт `data_parser.py` демонстрирует разбор данных персонажа из JSON-строки, полученной из Rick and Morty API.

## Описание

- JSON-строка загружается из файла `character_108.json`.
- Для демонстрации используется BeautifulSoup для обработки JSON.
- Затем JSON преобразуется в Python-объект.
- Извлекаются ключевые данные персонажа: ID, имя, статус, вид, тип, пол, происхождение, локация, URL изображения, количество эпизодов и ссылка на персонажа.
- Результат выводится в терминал.

## Как использовать

1. Убедитесь, что у вас установлен Python 3 и библиотеки:

`pip install beautifulsoup4`


2. Запустите парсер:

`python data_parser.py`


3. В терминале будет показан словарь с данными персонажа.

## Примечание

- Этот парсер служит примером раздельной обработки данных после получения JSON из API.

---


Документация Rick and Morty API доступна по ссылке:  
[https://rickandmortyapi.com/documentation/](https://rickandmortyapi.com/documentation/)

---

## Пример вывода данных

<img width="902" height="112" alt="image" src="https://github.com/user-attachments/assets/566f4a51-f376-45c4-9786-debee13de537" />
