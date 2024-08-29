@echo off
echo Installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt

echo Collecting static files...
python manage.py collectstatic --noinput
