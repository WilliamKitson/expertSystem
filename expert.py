from rule import Rule

class Expert:
    def __init__(self):
        self.rules = []
        self.facts = []

    def add_rule(self, conditions, conclusion):
        self.rules.append(Rule(conditions, conclusion))

    def investigate(self):
        unique_conditions = []

        for rule in self.rules:
            for condition in rule.conditions:
                if condition not in unique_conditions:
                    unique_conditions.append(condition)

        for unique_condition in unique_conditions:
            response = input(f"{unique_condition}? (yes/no): ")

            if response == 'yes':
                self.facts.append(unique_condition)

    def get_facts(self):
        return self.facts