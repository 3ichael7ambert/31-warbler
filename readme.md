# Warbler

## Readme

Due to posible version errors if erros occur while installing the requirements files

```bash
pip install -r requirements.txt
```

you may have to remove psycopg2-binary==2.8.4 and manually install the requirements

```bash
pip install psycopg2-binary
pip install psycopg2
```

I have also included a post_requirements_manual.md file so you may easily copy all requirements into the terminal

Further information
This should be the required procedure to initialize the app

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
createdb warbler
python seed.py
flask run
```

## Notes to developers

```bash
pip freeze > requirements.txt
```

### testing

```bash
psql
```

```sql
CREATE DATABASE warbler_test;
CREATE DATABASE "warbler-test";
```

```bash
FLASK_ENV=testing python -m unittest test_message_model.py
FLASK_ENV=testing python -m unittest test_message_views.py
FLASK_ENV=testing python -m unittest test_user_model.py
FLASK_ENV=testing python -m unittest test_user_views.py
```
