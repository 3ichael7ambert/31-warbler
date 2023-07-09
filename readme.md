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

#### DEPLOYMENT NOTES - PROCESS

##### SQL

1. Elephantsql.com
2. Create 'Tiny Turtle' free instance
3. Select region: US-West-1
4. copy related URL

to copy local database to Elephant sql run this script in the terminal

```bash
pg_dump -O warbler | psql (url you copied here)
```

then to check the database connection

```bash
psql (url you copied here)
```

##### Render.com

When we deploy an application in production,
we will always want to use a server that is production ready and not meant for just development.

```bash
pip install gunicorn
```

make sure to run this inside of the venv then update requirements.txt

```bash
pip freeze > requirements.txt
```

###### Steps

1. Create an account at [Render](https://render.com/) using GitHub
2. From dashboard, create a new instance of “Web service”
3. Connect to your repository
4. Give it a name *(this must be globally unique)*
5. Make sure the start command is `gunicorn app:app`
6. Choose advanced, and enter environmental variables:
    1. *DATABASE_URL*: URL from ElephantSQL (change `postgres:` → `postgresql:`)
    2. *SECRET_KEY*: anything you want *(to be secure: long and random)*
    3. *PYTHON_VERSION*: 3.X.X - whichever version you are using 
7.  Choose “Create Web Service”


