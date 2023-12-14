## Soap python service

SOAP (Simple Object Access Protocol) je protokol za razmenu 
strukturiranih informacija u distribuiranim računarskim 
sistemima. Koristi XML za formatiranje poruka i HTTP protokol
za prenos tih poruka. SOAP servisi omogućavaju komunikaciju između različitih sistema
putem standardizovanog i interoperabilnog formata poruka.

Spyne je Python biblioteka koja olakšava implementaciju
SOAP servisa. Omogućava definisanje servisa, metoda,
tipova podataka i protokola na jednostavan način.
Spyne generiše WSDL (Web Services Description Language) dokument koji opisuje strukturu i funkcionalnosti servisa, što omogućava kompatibilnost između različitih tehnologija.


### Project structure
- alembic (alembic data with versions)
- app (application inside logic)
- models (db models)
- utils (db utils)
- app/ env (env file with params)
- requirements.txt (reqs file)

### Run project



```commandline
- pip install -r requirements.txt
- alembic init
- populate alembic with correct path db info
- start main.py script (if make server used)
- hupper -m waitress --port=8000  main:app (if flask used)

```

Nakon pokretanja wsd dokument je dostupan na:

```python
http://127.0.0.1:8000?wsdl
```

### DB MIGRATIONS

Alat alembic je koriscen za migracije.
ALembic init fajl sadrzi url za konekciju na bazu (drajver, informacije)
```commandline
-  alembic revision --autogenerate -m "Init"

  Alembic revision creates new version migration with -m message (name of migration),
--autogenerate (automatically regarding models)

- alembig upgrade head (applies migration to the DB)

```

### SQLITE
```commandline


We use sqlite for demo purpose because of small memory usage and easy install,
any ORM - rel database can be connected

oracle+cx_oracle://<username>:<password>@<host>:<port>/<service_name_or_sid>


#NOTE
Spyne can't use uvicorn services cus it does not uses async http 
(asgi)