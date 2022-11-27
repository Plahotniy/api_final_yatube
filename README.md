# Api for YaTube
## Api based on Django_Rst_Framework


How to start a project:
Clone the repository and go to it on the command line:

git clone https://github.com/yandex-praktikum/kittygram_backend.git
cd kittygram_backend
Create and activate a virtual environment:

python3 -m venv env
If you have Linux/mac OS

source env/bin/activate
If you have windows

source env/scripts/activate
python3 -m pip install --upgrade pip
Install requirements from a file requirements.txt:

pip install -r requirements.txt
Make migrations:

python3 manage.py migrate
Start a project:

python3 manage.py runserver