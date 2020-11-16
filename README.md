# Challenge - Sucursal CRUD

[Enunciado](https://github.com/cassa10/challenge-api/blob/main/doc/software-engineer_challenge-1.pdf)

# Pre-Requirements:

- Python 3 
- Pip
- Django


# Installation

- Cd to repo main folder 
- Execute commands in order: 
    >python -m venv venv
    >venv\Scripts\activate
    >pip install django

# Set up and Start Server:

- Cd to repo main folder and then sucursal_crud.

- Create admin user with command: 
    >python manage.py createsuperuser"
    >Then complete inputs...

- Run Unit Test with command: 
    >python manage.py test --pattern="*Test.py"

- First time commands:
    >python manage.py makemigrations
    >python manage.py migrate

- Start server command:
    >python manage.py runserver

- Then go to browser at "http://localhost:8080"