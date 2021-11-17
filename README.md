# LJWE Database

Database setup and management scripts for LJWE trading system. Utilizes `alembic` to track revisions to database schema. Currently pulls data from Alpha Vantage in the following formats: intraday, daily, weekly, monthly. Data is reformatted using `pandas` and committed to the database using `SQLAlchemy`.

![database_schema](ljwedb.png)

The functions fall primary into two categories, retrievers, which query and format data from Alpha Vantage, and updaters, which take that data and update the database.

This database is used as part of a full stack application, and will be deployed on PostgreSQL during production.
