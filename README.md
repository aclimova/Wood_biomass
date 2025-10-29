# wood biomass

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

WOOD_BIOMASS — Анализ и обработка данных биомассы
Описание
Этот проект предназначен для анализа, обработки и хранения биотехнологических данных (биомасса, парсинг, работа с API и БД).

Структура проекта
text
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
Быстрый старт
Создать виртуальное окружение (пример для Windows):

text
python -m venv venv
venv\Scripts\activate
Установить зависимости:

text
pip install -r requirements.txt
Создать .env на основе шаблона:

text
copy .env_example .env
и заполнить нужные параметры.

Запустить основные скрипты:

Парсер данных:

text
python API_and_parse/parse_example/data_parser.py
Пример работы с API:

text
python API_and_parse/API_example/API_reader.py
Загрузка данных:

text
python wood_biomass/data_loader.py
Запись в базу:

text
python wood_biomass/write_to_db.py
Запустить Jupyter Notebook для анализа:

text
jupyter notebook notebooks/EDA.ipynb

