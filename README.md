# Шаблон репозитория, для успешной сдачи лабораторных работ.

## Введение
Данный шаблон является примером оформления кода для сдачи лабораторных работ.
Рекомендуется  строго его придерживаться во избежания проблем при сдаче и понижения баллов


## Структура проекта

 <pre>
lab1-2nd-semester/
│
├── src/
│   ├── protocols/
│   │   ├── __init__.py
│   │   └── protocols.py          # протоколы Task и TaskSource
│   │
│   ├── sources/
│   │   ├── __init__.py
│   │   ├── file_source.py         # источник из файла
│   │   ├── generator_source.py    # генератор задач
│   │   └── fake_api_source.py     # API
│   │
│   └── tasks/
│       ├── __init__.py
│       └── task.py                # Класс задачи
│
├── tests/
│   ├── __init__.py
│   ├── ...py
│   └── test_sources.py
│
├── config.json                     # конфигурация источников
├── main.py                         # точка входа
│
├── .gitignore
├── pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
</pre>

## Принцип работы
