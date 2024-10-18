# Names Project

File main.py exports names.csv to db.sqlite3 through DRF API. Browsable API allows users to create, edit and display folders and names.

## Project setup

### DB Migrations

`cd narvi && python manage.py migrate`

### Local server

`python manage.py runserver`

## names.csv

To export this file run `python main.py` in main folder. It will create names and folders for each prefix.
