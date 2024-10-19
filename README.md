# Flask Rule Engine with AST-based Rule Parsing

## Overview

This is a Python-based rule engine built using the Flask framework. The application allows users to define, combine, and evaluate rules using Abstract Syntax Trees (AST). Rules are represented as logical expressions (AND, OR, etc.) that can be evaluated against user-provided data. The application supports functionalities like rule creation, evaluation, and combining multiple rules into more complex expressions.

## Key Features:

- Create rules with logical conditions like (age > 30 AND department = 'Sales') OR (experience > 5).
- Evaluate rules against dynamic user data.
- Combine multiple rules using operators like AND, OR to create complex conditions.
- Supports AST-based rule storage in JSON format for efficient parsing and evaluation.
- Includes basic error handling, validation, and database integration using PostgreSQL and SQLAlchemy.

## Table of Contents
1. Installation
2. Project Structure
3. Database Setup
4. API Endpoints
5. Testing with Postman
6. Error Handling and Validation
7. License

# Installation
# Prerequisites
1. Python 3.x installed.
2. PostgreSQL installed and running.
3. pip for managing Python packages.
4. Postman (optional, for testing the API).

# 1. Clone the Repository

git clone https://github.com/muskansinghal26/rule_engine_api.git

cd rule-engine

# 2. Install Dependencies
Install the required Python libraries using pip:
pip install -r requirements.txt

# 3. Install PostgreSQL
Make sure you have PostgreSQL installed. You can download it from the official PostgreSQL website.

# 4. Set Up Environment Variables
Create a .env file in the root directory to store your database credentials. Example:
python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

# Project Structure
rule-engine/
├── app.py               # Entry point for the Flask app
├── ast_engine.py        # AST logic for rule creation, combination, and evaluation
├── routes.py            # API routes (create, combine, evaluate rules)
├── models.py            # Database models
├──test_api.py           # To run the tests
├── migrations/          # Database migration files
└── README.md            # Project documentation

- ast_engine.py
Contains the core logic for creating, evaluating, and combining rules. It defines the Node class which represents a rule or part of a rule in the Abstract Syntax Tree (AST).

- models.py
Defines the database model for storing rules using SQLAlchemy.

- routes.py
Contains the Flask routes that define the API endpoints for interacting with the rule engine.

- app.py
The main application file that initializes the Flask app and registers the API blueprint.

# Database Setup
Install PostgreSQL if you haven't already.

- Create the Database:
Open pgAdmin or use the PostgreSQL CLI to create a new database:

psql -U postgres

- Then, create a database and user (optional):
CREATE DATABASE rule_engine;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE rule_engine TO myuser;

- Configure the Flask App to Use PostgreSQL:

In db_config.py, ensure that the connection URL matches your PostgreSQL setup:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost/rule_engine'

### API Endpoints

#### Create Rule
- **URL**: `/create_rule`
- **Method**: POST
- **Payload**:
```json
{
 "rule": "age > 18 AND (income > 50000 OR credit_score > 700)"
}


   




