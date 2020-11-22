# Challenge - Sucursal CRUD

[Enunciado](https://github.com/cassa10/challenge-api/blob/main/doc/software-engineer_challenge-1.pdf)

# Pre-Requirements and modules

- Python 3 
- Pip
- Django
- PostgreSQL
- psycopg2-binary
- haversine
- drf-yasg (Swagger not deprecatted)
- bash (optional with docker and automated scripts)

More info [here](https://github.com/cassa10/challenge-api/blob/main/requirements.txt)

# Installation venv

- Cd to repo main folder 

- Execute commands in order: 
    - DEV (Optional)
        >python -m venv venv

# Set up and Start Server without Docker

### [PRECONDITION] Must set up all of list.env in your system env variables

- Cd to repo main folder and then sucursal_crud

- Create admin user with command:

    >python manage.py createsuperuser

    >Then complete inputs...

- Run Unit Test with command:

    >python manage.py test --pattern="*Test.py"

- Execute script "runAPI.sh" in folder where it belongs

## Script runAPI.sh explanation:

- If you have venv installed and folder initialized inside challenge-api folder, script executes with venv 

- If only updates models objects or do not have folder migrations in sucursal_crud_api:

    >python manage.py makemigrations sucursal_crud_api

- Create database entities

    >python manage.py migrate

- Start server command:
    
    >python manage.py runserver

- Then go to "http://localhost:8000"

# Docker

- Execute bash script "runDocker.sh" in folder where it belongs


# API Documentation

## Django administration 

### /admin

Frontend of django for administrate api and database objects

## Swagger 

### / or /api

If server is running, you could visit root endpoint API for Swagger DOCs and Skip this next docum

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




## Punto de Retiro 

###  /api/puntoDeRetiro

- GET

- POST

###  /api/puntoDeRetiro/<id\>

- GET

- PUT

- DELETE

## Query Near Node

### /api/nodo/cercano/<lat>/<lng>

- GET
    Parameters: "lat" y "lng"

    Desc: Get the nearest node of requested position

    
