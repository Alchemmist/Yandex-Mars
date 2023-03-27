# Yandex-Mars 🪐
Web приложение, созданное на 2-ом курсе Лицея Академии Янедкса, об освоении космоса и колонизации Марса.

## Запуск 🚀
1. Клонируйте репозиторий
```shell
git clone <https://github.com/Alchemmist/Yandex-Mars.git>
```

2. Перейдите в директорию проекта
```shell
cd Yandex-Mars
```

3. Установите зависимости
Это можно сделать с помощью `poetry` или стандартного `pip`

3.1 Poetry
```shell
poetry shell
poetry install
```

3.2 pip
```shell
python -m venv vevn
venv/Scripts/activate
pip install -r requirements.txt
```

4. Запуск на локальном хосте
```shell
cd app
python main.py
```

После выполнения всех пунктов в папке `db` появится файл базы данных: `blogs.db`
И в браузере откроется стартовая страница приложения
