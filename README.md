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


WOOD_BIOMASS/

│

├─ API_and_parse/

│   ├─ API_example/

│   │   ├─ API_reader.py

│   │   └─ README.md

│   └─ parse_example/

│       ├─ data_parser.py

│       └─ README.md

├─ data/

│   ├─ processed/

│   │   ├─ .gitkeep

│   │   └─ dataset_converted.parquet

│   └─ raw/

│       ├─ .gitkeep

│       └─ downloaded_dataset.csv

├─ notebooks/

│   ├─ .gitkeep

│   ├─ EDA.ipynb

│   └─ 00_project_overview.ipynb

├─ references/

│   └─ .gitkeep

├─ reports/

│   └─ figures/

│       ├─ .gitkeep

│       ├─ Downloading_the_df_on_provinces_into_the.png

│       └─ Loading_dataset_example.png

├─ wood_biomass/

│   ├─ __init__.py

│   ├─ data_loader.py

│   └─ write_to_db.py

├─ .env_example

├─ .gitignore

├─ Makefile

├─ README.md

├─ requirements.txt

└─ setup.cfg


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

## Автор, поддержка и лицензия

Автор проекта: **aclimova**  
Обратная связь: [GitHub Issues](https://github.com/aclimova/Wood_biomass/issues)  
Лицензия: MIT

---

## Примечания

- Все примеры переменных среды и команд даны для быстрой интеграции, детали — в комментариях к исходному коду.
- По всем вопросам и предложениям обращайтесь через Issues на GitHub.

---


