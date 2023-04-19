# yatube_project

## Yatube - это социальная сеть для блогеров. С БД SQLite и админкой сайта. Другие компоненты отсутствуют. 

# Установка
1. Склонируйте репозиторий:

``` git clone https://github.com/freddy7753/yatube_project.git ```

2. Установите зависимости:

``` python3 -m venv env && source env/bin/activate && pip install -r requirements.txt ```

3. Выполните миграции:

``` python manage.py migrate ```

4. Создайте суперпользователя:

``` python manage.py createsuperuser ```

5. Запустите сервер:

``` python manage.py runserver ```

# Использование
 Только через админку

