#!/bin/bash

# Executes API without Docker

# Evaluates if this script is executed in the same folder where it belongs.
if [ ! -d "./sucursal_crud" ] || [ -d "./sucursal_crud_api" ]
then
    echo "[ERROR] - Not executed at same level folder"
    echo "[INFO] - Execute script at same level folder where it belongs"
    exit 1
fi

# if exist venv folder, it uses venv for compilation. Otherwise await user agree with to execute without venv. 
if [ ! -d "./venv" ] 
then
    echo "[INFO] - Executing with venv"
    . venv/Scripts/activate
else
    echo "venv not found, are you sure to install dependencies without venv? (y/n)"
    read userAccept
fi 

# Evaluate user input contains 'y'
if [[ $userAccept != y* ]]
then
    echo "Your answer was \"$userAccept\" and it was considered as no. Try again when venv was installed and set up in project root folder"
    exit 2
fi

# Install dependencies
pip install --upgrade pip

pip install -r requirements.txt

# Go to app folder.
cd ./sucursal_crud

# Create database entities.
python manage.py migrate

# Start server.
python manage.py runserver 0.0.0.0:8000