# Names Project

File main.py exports names.csv to db.sqlite3 through DRF API. Browsable API allows users to create, edit and display folders and name.

## Project setup

### DB Migrations

`cd narvi && python manage.py migrate`

### Local server

`python manage.py runserver`

## names.csv

To export this file run `python main.py` in main folder. It will create names and folders for each prefix.

## Issues to solve

Currently there are some prefixes which contain the same names. Db has unique constraints, but names.csv won't be fully exported cause of this issue
