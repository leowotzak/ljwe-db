# LJWE Database

`SQLAlchemy` database setup and management scripts for the Master Securities Database. Utilizes `alembic` to track revisions to database schema and `pandas` to extract, transform, & load data. Requests asset price and metadata from [Alpha Vantage](https://www.alphavantage.co/) and automatically inserts into or updates the database.

This is used as part of a full stack application, and will is currently deployed with `PostgreSQL` on Heroku. The `ljwedb` module is a collection of scripts that perform the initialization and updating functions. Updates are scheduled to be run daily after the end of trading hours.

## Modules


### _**retrieve.py**_

---

Namespace of functions that retrieve and format data from alpha vantage

* Manufactures queries, and sends GET requests to alpha vantage. Extracted results are transformed into a format that is recognized and loaded by the database schema.

---

### _**update.py**_

Namespace of functions that update the Database

* Functions initialize a database session, request each alpha vantage endpoint, and insert/update new data.

---

### _**models.py**_

| Symbol Data | Interday Data | Intraday Data |
|----|----|----|
| symbol | daily | one minute |
|| weekly | five minute |
|| monthly | fifteen minute |
||| thirty minute |
||| sixty minute |

![database_schema](ljwedb.png)

Learn more: (https://www.leojwotzak.com)
