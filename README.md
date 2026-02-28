# Лабораторная работа №6
* **
## Цель:
* Освоить duck typing и контрактное программирование на примере источников
задач.
* **

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
* **
## Суть системы
Это подсистема приёма задач в платформе обработки задач (типо).
Использует она 3 источника: генератор, api (псевдоапи) и чтение из файла.
Она получает задачи и выводит их в консоль
* **
## Как с ней работать?
Есть файл по директории: src/config.json. По ключу "sources" можно вписывать источники ("type"). Их всего 3 типа:
1) "api". Требует "url" (ссылку).
2) "generator". Ничего не требует
3) "file". Требует "path" (путь)

Пример config.json:
<pre>
{
  "sources": [
    {"type": "api", "url": "sss"},
    {"type": "file", "path": "file.txt"},
    {"type": "generator"}
  ]
}
</pre>
* **
## Протоколы и классы
### protocols.py
Реализует 2 основных протокола:
- **TaskProtocol** - представляет задачу. Датакласс. Имеет поля id: int, payload: Any
- **TaskSource** - представляет источник задач. <br>Имеет метод get_tasks(self) -> List[TaskProtocol]
### task.py
Реализован класс Task, который следует протоколу TaskProtocol
### fake_api_source.py
Класс FakeApiSource эмулирует получение задач через API:
* При инициализации принимает url
* Метод get_tasks генерирует 10 тестовых задач со случайными данными
* Каждая задача оборачивается в объект Task с uuid4.int
### file_source.py
Класс FileSource читает задачи из текстового файла:
* При открытии проверяет существование файла, иначе FileNotFoundError
* Метод get_tasks построчно читает файл, создавая задачу из каждой строки
* __del__() автоматически закрывает файл при уничтожении объекта
* Аналогично задачи оборачиваются Task с uuid4.int
### generator_source.py
Генерирует случайные задачи
* По работе похожа на fakeapi, но тут абсолютный рандом, payload может быть str, list или json
* Не требует аргументов при инициализации
