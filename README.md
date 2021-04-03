# py-webapp-sandbox
Sandbox to play around with ideas on how to build sustainable Python web application.

## Setup
1. Pull down the app from version control
1. Make sure you create and activate your local virtual env 
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```
1. `bin/setup`

## Running the app

1. `bin/run`

## Tests and CI
1. `bin/ci` contains all the tests and checks for the app


## Database

### Create a Migration Script
1. [Create a migration](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script) 
    ```bash
    alembic revision -m "create albums table"
    ```
1. Fill in the `upgrade()` and `downgrade()` methods
1. Apply the migration
    ```bash
    alembic upgrade head
    ```

To [revert](https://alembic.sqlalchemy.org/en/latest/tutorial.html#relative-migration-identifiers) the latest migration applied, run
```bash
alembic downgrade -1
```

### Update `models.py`
1. `bin/db-reflect`
