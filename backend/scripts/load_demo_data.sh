#!/bin/bash

echo "Loading data from dump.json. This will delete all existing data."
echo

read -p "Do you want to proceed? [Y/N]: " choice
if [[ $choice != [Yy] ]]; then
    echo "Operation cancelled."
    exit 0
else
    docker exec -it shipmentstest-backend python manage.py flush --no-input
    docker exec -it shipmentstest-backend python manage.py loaddata dump.json
    echo "Done."
fi
