# ast_engine.py
import uuid

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.id = str(uuid.uuid4())
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'value': self.value,
            'left': self.left.to_dict() if isinstance(self.left, Node) else self.left,
            'right': self.right.to_dict() if isinstance(self.right, Node) else self.right
        }

    @classmethod
    def from_dict(cls, data):
        node = cls(data['type'], data.get('value'))
        node.id = data.get('id', str(uuid.uuid4()))  # Generate a new ID if not provided
        if isinstance(data.get('left'), dict):
            node.left = cls.from_dict(data['left'])
        else:
            node.left = data.get('left')
        if isinstance(data.get('right'), dict):
            node.right = cls.from_dict(data['right'])
        else:
            node.right = data.get('right')
        return node

def create_rule(rule_str):
    # This is a simple parser. You might want to use a more robust parsing method for complex rules.
    parts = rule_str.split('AND')
    if len(parts) > 1:
        return Node('AND', left=create_rule(parts[0].strip()), right=create_rule(' AND '.join(parts[1:]).strip()))
    
    parts = rule_str.split('OR')
    if len(parts) > 1:
        return Node('OR', left=create_rule(parts[0].strip()), right=create_rule(' OR '.join(parts[1:]).strip()))
    
    # Simple condition
    if '>' in rule_str:
        left, right = rule_str.split('>')
        return Node('>', value=left.strip(), right=Node('VALUE', value=right.strip()))
    
    if '<' in rule_str:
        left, right = rule_str.split('<')
        return Node('<', value=left.strip(), right=Node('VALUE', value=right.strip()))
    
    if '==' in rule_str:
        left, right = rule_str.split('==')
        return Node('==', value=left.strip(), right=Node('VALUE', value=right.strip()))
    
    # If no operator is found, treat it as a simple condition
    return Node('CONDITION', value=rule_str.strip())

def evaluate_rule(rule, user_data):
    if rule.type == 'AND':
        return evaluate_rule(rule.left, user_data) and evaluate_rule(rule.right, user_data)
    elif rule.type == 'OR':
        return evaluate_rule(rule.left, user_data) or evaluate_rule(rule.right, user_data)
    elif rule.type == '>':
        left_value = user_data.get(rule.value)
        right_value = float(rule.right.value)
        return left_value > right_value if left_value is not None else False
    elif rule.type == '<':
        left_value = user_data.get(rule.value)
        right_value = float(rule.right.value)
        return left_value < right_value if left_value is not None else False
    elif rule.type == '==':
        left_value = user_data.get(rule.value)
        return left_value == rule.right.value if left_value is not None else False
    elif rule.type == 'VALUE':
        return rule.value
    else:
        raise ValueError(f"Unknown rule type: {rule.type}")

    
def combine_rules(rule1, rule2, operator):
    if operator.upper() not in ['AND', 'OR']:
        raise ValueError("Operator must be 'AND' or 'OR'")
    return Node(operator.upper(), left=rule1, right=rule2)