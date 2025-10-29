# Rick and Morty API Reader

Этот скрипт `api_reader.py` делает запрос к Rick and Morty API и загружает данные о персонаже по заданному ID.

## Описание

- Используется библиотека `requests` для HTTP-запроса.
- Загружаются данные персонажа в формате JSON с API https://rickandmortyapi.com/api/character/108.
- Полученные данные сохраняются в локальный файл `character_108.json` в JSON-формате.

## Как использовать

1. Убедитесь, что установлен Python 3 и библиотека requests:

`pip install requests`


2. Запустите скрипт:

`python api_reader.py`


3. После успешного выполнения в папке появится файл `character_108.json` с данными персонажа с ID 108 (Dr. Xenon Bloom).

## Функции

- `fetch_character_data(character_id)` — получает данные по указанному ID персонажа.
- В блоке `if __name__ == "__main__"` вызывается загрузка и сохранение данных в файл.

---

## Дополнительно

Можно изменять ID персонажа, передавая другой параметр в функцию `fetch_character_data`.

Полная документация API доступна на: [Rick and Morty API Documentation](https://rickandmortyapi.com/documentation/)
