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
git clone https://github.com/omkar-dsd/work_japan_companies.git
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
python manage.py makemigrations
```

6. Migrate the generated migrations
```python
python manage.py migrate
```

7. Run the applciation
```python
python manage.py runserver
```

> Note: The server will start on localhost:8000 (the default django port).

## API End Points

### List or Create

```bash
http://127.0.0.1:8000/postal_addresses/
```


```bash
http://127.0.0.1:8000/companies/
```

### Details or Update or Delete

To get the details, or the panel to update or delete a particular record, pass the primary key of the record in the following manner

```bash
http://127.0.0.1:8000/postal_addresses/1/
```


```bash
http://127.0.0.1:8000/companies/1/
```

OR


```bash
http://127.0.0.1:8000/postal_addresses/?pk=1
```


```bash
http://127.0.0.1:8000/companies/?pk=1
```

The panel provides option to update or delete the existing record.

### Filters
> :warning: Filters are case sensitive

- Filter by company name
```bash
http://127.0.0.1:8000/companies/filter/?name=work_japan
```
Sample Response:
```json
{
  "status": 200,
  "total": 1,
  "companies": [
    {
      "name": "work_japan",
      "building_number": 777,
      "postal_code": 1000001,
      "locality": "A Street",
      "city": "Tokyo",
      "state": "State Tokyo"
    }
  ]
}
```

- Filter by city
```bash
http://127.0.0.1:8000/companies/?city=Tokyo
```
Sample Response:
```json
{
  "status": 200,
  "total": 2,
  "companies": [
    {
      "name": "work_japan",
      "building_number": 777,
      "postal_code": 1000001,
      "locality": "A Street",
      "city": "Tokyo",
      "state": "State Tokyo"
    },
    {
      "name": "XYZ",
      "building_number": 123,
      "postal_code": 1000002,
      "locality": "B Street",
      "city": "Tokyo",
      "state": "State Tokyo"
    }
  ]
}
```


- Filter postal codes which have more than X number of companies
```bash
http://127.0.0.1:8000/companies/?count=2
```
 Sample Response:
 ```json
 {
  "status": 200,
  "total": 3,
  "postal_codes": [
    8000,
    9000,
    1000001
  ]
}
```
> :warning: Note: The integer passed is not inclusive.  
