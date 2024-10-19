import requests  # type: ignore
import json

BASE_URL = "http://localhost:5000/api"

def test_create_rule():
    url = 'http://localhost:5000/create_rule'
    payload = {
        'rule': 'age > 18 AND (income > 50000 OR credit_score > 700)'
    }
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    try:
        data = response.json()
        print("Create Rule Response:", data)
        return data['rule']['id']  # Return the id of the root node
    except json.JSONDecodeError:
        print("Could not decode JSON. Raw response:", response.text)
        return None

def test_evaluate_rule(rule_id):
    url = 'http://localhost:5000/evaluate_rule'
    payload = {
        'rule': {'id': rule_id, 'type': 'AND', 'value': None,
                 'left': {'type': '>', 'value': 'age', 'left': None, 'right': {'type': 'VALUE', 'value': '18'}},
                 'right': {'type': 'OR', 'value': None,
                           'left': {'type': '>', 'value': 'income', 'left': None, 'right': {'type': 'VALUE', 'value': '50000'}},
                           'right': {'type': '>', 'value': 'credit_score', 'left': None, 'right': {'type': 'VALUE', 'value': '700'}}}
                },
        'user_data': {'age': 25, 'income': 60000, 'credit_score': 750}
    }
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    try:
        data = response.json()
        print("Evaluate Rule Response:", data)
    except json.JSONDecodeError:
        print("Could not decode JSON. Raw response:", response.text)

def test_combine_rules(rule_id_1, rule_id_2):
    url = 'http://localhost:5000/combine_rules'
    payload = {
        'rule1': {'id': rule_id_1, 'type': 'CONDITION', 'value': 'age > 18', 'left': None, 'right': None},
        'rule2': {'id': rule_id_2, 'type': 'CONDITION', 'value': 'income > 50000', 'left': None,  'right': None},
        'operator': 'AND'
    }
    response = requests.post(url, json=payload)
    print("Combine Rules Response:", response.json())

if __name__ == "__main__":
    rule_id_1 = test_create_rule()
    rule_id_2 = test_create_rule()
    
    if rule_id_1 and rule_id_2:
        test_evaluate_rule(rule_id_1)
        test_combine_rules(rule_id_1, rule_id_2)
    else:
        print("Failed to create rules. Check the server logs for more information.")

if __name__ == "__main__":
    # Create two rules
    rule_id_1 = test_create_rule()
    rule_id_2 = test_create_rule()

    if rule_id_1 and rule_id_2:
        # Evaluate the first rule
        test_evaluate_rule(rule_id_1)

        # Combine the two rules
        combined_rule_id = test_combine_rules(rule_id_1, rule_id_2)

        if combined_rule_id:
            # Evaluate the combined rule
            test_evaluate_rule(combined_rule_id)
    else:
        print("Failed to create rules. Check the server logs for more information.")