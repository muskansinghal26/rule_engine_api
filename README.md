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
- **Description**: Creates a new rule and stores it in the database.
- **Request Body (JSON)**:
{
 "rule": "age > 18 AND (income > 50000 OR credit_score > 700)"
}

- **Response**: Returns the created rule as a JSON object

#### Evaluate Rule
- **URL**: `/evaluate_rule`
- **Method**: POST
- **Payload**:
- **Description**: Evaluates a stored rule against provided user data.
- **Request Body (JSON)**:
  {
  "rule": {
    "id": "rule_id",
    "type": "AND",
    "value": null,
    "left": {"type": ">", "value": "age", "left": null, "right": {"type": "VALUE", "value": "18"}},
    "right": {"type": "OR", "value": null,
              "left": {"type": ">", "value": "income", "left": null, "right": {"type": "VALUE", "value": "50000"}},
              "right": {"type": ">", "value": "credit_score", "left": null, "right": {"type": "VALUE", "value": "700"}}}
  },
  "user_data": {"age": 25, "income": 60000, "credit_score": 750}
}

- **Response**: Returns the evaluation result (true/false)

#### Combine Rule
- **URL**: `/combine_rules`
- **Method**: POST
- **Payload**:
- **Description**: Combines two existing rules into one using a logical operator (AND, OR).
- **Request Body (JSON)**:
  {
  "rule1": {"id": "rule_id_1", "type": "CONDITION", "value": "age > 18", "left": null, "right": null},
  "rule2": {"id": "rule_id_2", "type": "CONDITION", "value": "income > 50000", "left": null,  "right": null},
  "operator": "AND"
}

- **Response**:  Returns the combined rule as a JSON object.

##Testing with Postman
- Install Postman from here.

- Create a new request in Postman:

**URL**: http://127.0.0.1:5000/api/create_rule
**Method**: POST
**Body**: Select raw and choose JSON, then add the following JSON:
{
  "rule": "((age > 30 AND department = 'Sales') OR experience > 5)"
}

- Test the Rule Evaluation:

**URL**: http://127.0.0.1:5000/api/evaluate_rule
**Method**: POST
**Body**: Use JSON like:
{
  "rule_id": 1,
  "user_data": {
    "age": 35,
    "department": "Sales",
    "experience": 4
  }
}

##Error Handling and Validation
- **Invalid Rule Strings**: If the rule string has mismatched parentheses or invalid tokens, the system will return an error response with details:
  {
  "message": "Mismatched parentheses in rule string.",
  "status": "error"
}

- **Rule Not Found**: If you attempt to evaluate or combine a rule that doesn’t exist.
  {
  "message": "Rule not found",
  "status": "error"
}

**Empty Data**: Both rule creation and evaluation check for empty or missing data in the request payload.

## Testing

To run the tests, execute the following command:

python test_api.py

## Contributing
We welcome contributions to the Rule Engine! Please follow these steps:

1.Fork the repository.
2.Create a new branch (git checkout -b feature/YourFeature).
3.Make your changes and commit them (git commit -m 'Add your feature').
4.Push to the branch (git push origin feature/YourFeature).
5.Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to the contributors and the open-source community for their support and inspiration.


This README provides a more detailed overview of your rule engine application, including its features, tech stack, project structure, installation, usage, and core components. It also includes information on testing, contributing, licensing, and contact details.


