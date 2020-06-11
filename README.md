## Evironment
- python: 3.7.3
## Setup
```bash
$ virtualenv venv
$ source venv/bin/activate
$ cd configs/
$ touch configs/settings/local_settings.py
$ pip install -r requirements.txt
$ python manage migate
$ python manage runserver
```
###Testing
```bash
$ pytest
```

### lint and check code
Docs: http://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
```bash
$ pycodestyle --exclude migrations --show-source --show-pep8 puppies

# OR

# to lint all module
$ python manage.py lint_code
```
admin compilemessages
```
