# Electrify Task

## Setup

1. Set up a virtual environment: `python -m venv venv`
2. Activate your virtual environment: `source venv/bin/activate`
3. Install necessary packages: `pip install Django requests responses python-dotenv pytest`
4. Copy the example.env and add the API keys into the .env `cp example.env .env`

## Running Tests

1. Navigate to the directory containing the tests: `pytest tests`

## Running the Django App

1. Run the Django server: `python manage.py runserver`