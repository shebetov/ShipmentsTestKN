@echo off
echo Loading data from dump.json. This will delete all existing data.
echo.

choice /M "Do you want to proceed?"
if errorlevel 2 goto :no
if errorlevel 1 goto :yes

:no
echo Operation cancelled.
exit /b

:yes
docker exec -it shipmentstest-backend python manage.py flush --no-input
docker exec -it shipmentstest-backend python manage.py loaddata dump.json
echo Done.
