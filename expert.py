from rule import Rule

class Expert:
    def __init__(self):
        self.rules = []
        self.facts = []

    def add_rule(self, conditions, conclusion):
        self.rules.append(Rule(conditions, conclusion))

    def investigate(self):
        for unique_condition in self.calculate_unique_conditions():
            if input(f"{unique_condition}? (yes/no): ") == 'yes':
                self.facts.append(unique_condition)

    def calculate_unique_conditions(self):
        output = []

        for rule in self.rules:
            for condition in rule.conditions:
                if condition not in output:
                    output.append(condition)

        return output

    def get_facts(self):
        return self.facts

    def infer(self):
        for rule in self.rules:
            if all(fact in self.facts for fact in rule.conditions):
                return rule.conclusion