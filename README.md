# Work Japan - Companies API
API to manage various company addresses
## Platform

- Django 1.11
- Python 3.6
- PostgreSql
- Django Rest Framework

## Set up

1. Clone the project from git repository
```bash
git clone some_link_here
```
2. Go into root directory
```bash
cd work_japan_companies
```

3. Initialise `virtualenv` with python 3.6
```bash
virtualenv -p python3.6 venv
```

4. Install requirements into `virtualenv`
```bash
pip install -r requirements.txt
```

5. Make migrations
```python
python manage.y makemigrations
```

6. Migrate the generated migrations
```python
python manage.py migrate
```

7. Run the applciation
```python
python manage.py runserver
```

## API End Points

### List or Create

```bash
http://127.0.0.1:8000/postal_addresses/
```


```bash
http://127.0.0.1:8000/companies/
```

### Details or Update or Delete

```bash
http://127.0.0.1:8000/postal_addresses/
```


```bash
http://127.0.0.1:8000/companies/
```

### Filters

- Filter by company name
```bash
http://127.0.0.1:8000/companies/filter/?name=work_japan
```

- Filter by city
```bash
http://127.0.0.1:8000/companies/?city=tokyo
```

- Filter postal codes which have more than X number of companies
```bash
http://127.0.0.1:8000/companies/?count=2
```

> :warning: Note: The integer passed is not inclusive.  
