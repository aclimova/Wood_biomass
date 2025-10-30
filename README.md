# wood biomass

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

# WOOD_BIOMASS — Анализ и обработка данных древесной биомассы

Описание

Этот проект предназначен для анализа, обработки и хранения биотехнологических данных (биомасса, парсинг, работа с API и БД).

Модульный проект для организации биотехнологической обработки древесной биомассы. Реализует классический процесс ETL: загрузка, валидация, трансформация и импорт данных в базу данных.

---

## Структура проекта

<pre> <code> WOOD_BIOMASS/ 
    │ 
    ├── .env files/ # Файлы переменных среды 
    │ ├── .env # Основные переменные среды для БД 
    │ └── example.env # Пример переменных (без данных) 
    │ 
    ├── API_and_parse/ # Работа с API и парсингом данных 
    │ ├── API_example/ 
    │ │ ├── API_reader.py # Скрипт для чтения данных через API 
    │ │ └── README.md # Инструкция по API 
    │ └── parse_example/ 
    │ ├── data_parser.py # Скрипт для парсинга данных 
    │ └── README.md # Инструкция по парсингу 
    │ 
    ├── data/ # Все рабочие (сырые, очищенные, преобразованные) данные 
    │ ├── API_and_parse/ 
    │ │ └── character_108.json # JSON с результатами парсинга 
    │ ├── converted_ds/ 
    │ │ └── dataset_converted.parquet # Готовый датасет 
    │ └── raw_ds/ 
    │ └── downloaded_dataset.csv # Сырые данные 
    │ 
    ├── etl/ # Главные ETL-скрипты 
    │ ├── extract.py # Extract (выгрузка) 
    │ ├── validate.py # Validate (валидация) 
    │ ├── transform.py # Transform (преобразование)
    │ ├── load.py # Load (загрузка в БД) 
    │ └── main.py # Управляющий скрипт ETL 
    │ 
    ├── notebooks/ # Jupyter/EDA-ноутбуки 
    │ ├── EDA.figures/ # Визуализации и графики для анализа 
    │ │ ├── *.png # Картинки с результатами EDA 
    │ ├── .gitkeep # Для хранения пустых папок в Git 
    │ └── EDA.ipynb # Основной EDA-ноутбук 
    │ 
    ├── reports/ # Отчёты и презентационные материалы 
    │ ├── figures/ 
    │ │ ├── *.png # Картинки для отчётов 
    │ │ └── .gitkeep 
    │ └── .gitkeep 
    │ 
    ├── wood_biomass/ # Пакет проекта (если нужен импорт) 
    │ └── __init__.py 
    ├── .gitignore 
    ├── Makefile 
    ├── README.md 
    ├── requirements.txt 
    └── setup.cfg </code> </pre>




---

## Быстрый старт

1. **Клонирование репозитория и установка зависимостей:**
    ```
    git clone https://github.com/aclimova/Wood_biomass.git
    cd Wood_biomass
    pip install -r requirements.txt
    ```

2. **Заполнение .env:**
    - Скопируйте `.env.example` → `.env`, заполните ваши параметры PostgreSQL.

3. **Запуск ETL:**
    ```
    python etl/main.py
    ```
    - После запуска: данные будут загружены, проверены, преобразованы и записаны в базу данных.

---

## Основные модули

- **extract.py**: Автоматическая загрузка исходного файла (например, из Google Drive) и сохранение его по пути `data/raw_ds/downloaded_dataset.csv`.
- **validate.py**: Проверка на пустоту, обязательные поля, типы данных и дубликаты.
- **transform.py**: Восстановление пропусков, перевод типов (str→category, float→numeric) и финальная подготовка набора.
- **load.py**: Импорт в PostgreSQL, настройка подключения через переменные среды (в `.env`).

---

## Данные

**Исходный деревесный датасет:**  
[Biomass Data](https://drive.google.com/drive/folders/1TOftr_GOVv2wXgeg4S5GTd46YWDHC2Ls?usp=drive_link)

[Расширенная и интерактивная визуализация EDA на nbviewer](https://nbviewer.org/github/aclimova/Klimova-75-63-project/blob/main/notebooks/EDA.ipynb?flush_cache=true)

[Расширенная и интерактивная визуализация EDA на GoogleColab](https://colab.research.google.com/github/aclimova/Klimova-75-63-project/blob/main/notebooks/EDA.ipynb)

## Автор, поддержка и лицензия

Автор проекта: **aclimova**  
Обратная связь: [GitHub Issues](https://github.com/aclimova/Wood_biomass/issues)  
Лицензия: MIT

---

## Примечания

- Все примеры переменных среды и команд даны для быстрой интеграции, детали — в комментариях к исходному коду.
- По всем вопросам и предложениям обращайтесь через Issues на GitHub.

---


