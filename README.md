## Evironment
- python: 3.7.3
## Setup

```
$ virtualenv venv
$ source venv/bin/activate
$ cd configs/
$ touch configs/settings/local_settings.py
$ pip install -r requirements.txt
$ python manage migate
$ python manage runserver
```
##Testing

```
$ pytest
```

## Lint and check code

Docs: http://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
```
$ pycodestyle --exclude migrations --show-source --show-pep8 puppies
# OR
# to lint all module
$ python manage.py lint_code
```

## Migrate Database

```
$ python manage.py makemigrations $app_name
$ python manage.py migrate
```

## Run Project

```
$ python manage.py runserve

# API Doc
## http://localhost:8000/ or http://127.0.0.1:8000/

# Template Todo
## http://localhost:8000/todo or http://127.0.0.1:8000/todo
```