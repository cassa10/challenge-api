# Challenge - Sucursal CRUD

[Enunciado](https://github.com/cassa10/challenge-api/blob/main/doc/software-engineer_challenge-1.pdf)

# Pre-Requirements

- Python 3 
- Pip
- Django


# Installation

- Cd to repo main folder 
- Execute commands in order: 
    >python -m venv venv
    >venv\Scripts\activate
    >pip install django

# Set up and Start Server

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

- Then go to "http://localhost:8000"


# API Documentation

Optional: If server is running, you could visit every endpoint with UI

## Sucursal

###  /api/sucursal

- GET

    Desc: Get all sucursals (paginated not contemplated)

- POST 

    Desc: Create new sucursal

### /api/sucursal/<id\>

- GET

    Desc: Get sucursal with requested id

- PUT

    Desc: Update sucursal with requested id and data provided

- DELETE

    Desc: Delete sucursal with requested id (logic deleted not contemplated)

    

---------

## Punto de Retiro 

###  /api/puntoDeRetiro

- GET

- POST

###  /api/puntoDeRetiro/<id\>

- GET

- PUT

- DELETE
