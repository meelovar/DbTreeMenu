# Запуск

- создать и активировать виртуальное окружение, установить Django необходимой
  версии из файла requirements.txt
```shell
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
- выполнить миграции БД
```shell
python manage.py migrate
```
- проинициализаровать БД из фикстуры
```shell
python manage.py loaddata ./menu/fixtures/initial.json
```
- создать суперпользователя
```shell
python manage.py createsuperuser
```
- запустить сервер
```shell
python manage.py runserver
```
