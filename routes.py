# routes.py

from flask import Blueprint, request, jsonify
from ast_engine import Node, create_rule, evaluate_rule, combine_rules

api = Blueprint('api', __name__)

@api.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    payload = request.get_json()
    rule = create_rule(payload['rule'])
    if rule is None:
        return jsonify({'error': 'Failed to create rule'}), 400
    return jsonify({'rule': rule.to_dict()})

@api.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    payload = request.get_json()
    try:
        rule = Node.from_dict(payload['rule'])
        user_data = payload['user_data']
        result = evaluate_rule(rule, user_data)
        return jsonify({'result': result})
    except KeyError as e:
        return jsonify({'error': f"Missing key in payload: {str(e)}"}), 400
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@api.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    payload = request.get_json()
    rule1 = Node.from_dict(payload['rule1'])
    rule2 = Node.from_dict(payload['rule2'])
    combined_rule = combine_rules(rule1, rule2, payload['operator'])
    return jsonify({'rule': combined_rule.to_dict()})