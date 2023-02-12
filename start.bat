@echo off
rem Activate the virtual environment
.env\Scripts\activate

@Rem Run App Migrations
python manage.py makemigrations
python manage.py migrate

rem Run the Django development server
start python manage.py runserver & start http://127.0.0.1:8000/
rem Open the app in a browser