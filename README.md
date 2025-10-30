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
├── .env files/
│   ├── .env              # Основные переменные среды для работы с БД и API (не публикуется на GitHub)
│   └── example.env       # Пример переменных для настройки, без личных данных
│
├── API_and_parse/        # Модуль для работы с внешними API, парсинга файлов и интеграций
│   ├── API_example/
│   │   ├── API_reader.py     # Скрипт для чтения данных через API 
│   │   └── README.md         # Описание конкретного API-примера
│   └── parse_example/
│       ├── data_parser.py    # Скрипт для парсинга/очистки данных из неструктурированных источников
│       └── README.md         # Описание парсинга, инструкции
│
├── data/                  # Все рабочие данные проекта (чистые, преобразованные, исходные)
│   ├── API_and_parse/
│   │   └── character_108.json        # Вспомогательные JSON-данные из API/парсера
│   ├── converted_ds/
│   │   └── dataset_converted.parquet # Финальный преобразованный датасет для анализа
│   └── raw_ds/
│       └── downloaded_dataset.csv    # Сырые исходные данные (из Google Drive)
│
├── etl/                    # Главный ETL-процессинг: автоматизация всех этапов
│   ├── extract.py          # Загрузка (Extract) сырых данных из внешних источников
│   ├── validate.py         # Проверка (Validate) структуры, типов, пропусков
│   ├── transform.py        # Преобразование (Transform): обработка, нормализация, подготовка
│   ├── load.py             # Загрузка (Load) в базу данных (PostgreSQL)
│   ├── main.py             # Управляющий сценарий, объединяющий все этапы ETL
│
├── notebooks/              # Jupyter/EDA-ноутбуки для исследовательского анализа, визуализации
│   ├── EDA.figures/        # Готовые картинки для отчётов и презентаций
│   │   ├── attribute density.png
│   │   ├── boxplots.png
│   │   ├── correlations btw numerical features.png
│   │   ├── facetgrid.png
│   │   ├── histogrammes.png
│   │   ├── stripplot.png
│   │   └── violin plot.png
│   ├── .gitkeep            # Технический файл для хранения пустых папок в Git
│   └── EDA.ipynb           # Основной ноутбук для разведочного анализа данных (EDA)
│
├── reports/                # Папка для отчётов, результатов, иллюстраций (например, для публикаций или презентаций)
│   ├── figures/
│   │   ├── .gitkeep
│   │   ├── Downloading into the central db.png        # Примеры загрузки и визуализации
│   │   └── Loading dataset example.png                # Иллюстрации работы ETL
│   └── .gitkeep
│
├── wood_biomass/           # Основной пакет приложения (Python package)
│   └── __init__.py         # Инициализация пакета для импорта функций на проекте
│
├── .gitignore              # Файл с перечнем игнорируемых для Git файлов/папок (.env, .pyc, data и т.д.)
├── Makefile                # Автоматизация типовых задач (например, установка, запуск тестов, сборка), если используется
├── README.md               # Описание проекта, инструкции по установке и запуску, ссылки
├── requirements.txt        # Список всех используемых библиотек (pip install -r requirements.txt)
└── setup.cfg               # Конфигурация для сборки, публикации, форматирования (можно использовать для PyPI) </code> </pre>




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


