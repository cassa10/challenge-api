# Challenge - Sucursal CRUD

[Enunciado](https://github.com/cassa10/challenge-api/blob/main/doc/software-engineer_challenge-1.pdf)

# Pre-Requirements and modules

- bash (optional for automated scripts)
- Docker (optional and *highly recommended*)
- Python 3 
- Pip
- Django
- PostgreSQL
- psycopg2-binary
- haversine
- drf-yasg (Swagger not deprecatted)

More info [here](https://github.com/cassa10/challenge-api/blob/main/requirements.txt)

# Set up and run API locally (without Docker)

## Installation venv (DEV / Optional)

- Cd to repo main folder 

- Execute:

    >python -m venv venv

- Then check "venv" folder must be in repo main folder

### [PRECONDITION] Must set up all of envs listed at "list.env" in your system env variables

- Cd to repo main folder 

- Cd to sucursal_crud (top-level)

- Create admin user

    >python manage.py createsuperuser

    >Then complete inputs...

- Run Unit Test

    >python manage.py test

- Run API

    > Cd to repo root folder

    > Execute script "runAPI.sh"


- Use API
    
    >Browse to "http://localhost:8000"

(If port 8000 is not free)

> Open script runAPI.sh

> Change it and save script

(If only updates models objects or do not have folder migrations in sucursal_crud_api)

>Cd to sucursal_crud (top-level) 

>python manage.py makemigrations sucursal_crud_api

## High-level explanation of runAPI.sh

- If you have venv installed and folder initialized inside challenge-api folder, script executes with venv. Otherwise wonder if you want to execute without venv.

- Upgrade pip and install dependencies

- Create database entities

- Start server command

# Set up and run API with Docker

- Cd to repo main folder

- Execute bash script "runDocker.sh"

- Create admin user (containers must be running)
    
    >docker-compose exec web python manage.py createsuperuser

- Run Unit Test (containers must be running)

    >docker-compose exec web python manage.py test

- Execute any command inside containers

    >docker-compose exec web <*command*>

(If you need another container config, edit docker-compose.yml file)

## High-level explanation of runDocker.sh

- Build image of API

- Execute docker compose and start containers with configuration at docker-compose.yml

------------

# API Documentation

## Django administration 

### /admin

Frontend of django for administrate api and database objects

Must have admin user for use it

## Swagger 

### / or /api

If server is running, you could visit root endpoint API for Swagger DOCs

## Sucursal

###  /api/sucursal

- GET
    
    Get all sucursal objects (no pagination)

- POST 

    Create new sucursal

### /api/sucursal/<id\>

- GET

    Get sucursal with requested id

- PUT

    Update sucursal with requested id and data provided

- DELETE

    Delete sucursal with requested id (logic deleted not contemplated)


## Punto de Retiro 

###  /api/puntoDeRetiro

- GET
    
    Get all puntoDeRetiro objects (no pagination)

- POST

    Create new puntoDeRetiro

###  /api/puntoDeRetiro/<id\>

- GET

    Get puntoDeRetiro with requested id

- PUT

    Update puntoDeRetiro with requested id and data provided

- DELETE

    Delete puntoDeRetiro with requested id (logic deleted not contemplated)

## Near Node

### /api/nodo/cercano/<*lat*>/<*lng*>

- GET

    Desc: Get the nearest node of requested location (latitude and longitude)



    
