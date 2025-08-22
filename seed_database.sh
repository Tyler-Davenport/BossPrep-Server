#!/bin/bash

rm db.sqlite3
rm -rf ./BossPrepapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations BossPrepapi
python3 manage.py migrate BossPrepapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

