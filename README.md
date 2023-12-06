## Soap python service
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

```


### DB MIGRATIONS
--  alembic revision --autogenerate -m "Init"
```commandline
Alembic revision creates new version migration with -m message (name of migration),
--autogenerate (automatically regarding models)

- alembig upgrade head (applies migration to the DB)

```

### SQLITE
```commandline


We use sqlite for demo purpose because of small memory usage and easy install,
any ORM - rel database can be connected

oracle+cx_oracle://<username>:<password>@<host>:<port>/<service_name_or_sid>
