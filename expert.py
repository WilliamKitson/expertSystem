from rule import Rule

class Expert:
    def __init__(self):
        self.rules = []

    def add_rule(self, conditions, conclusion):
        self.rules.append(Rule(conditions, conclusion))

    def investigate(self):
        unique_conditions = []

        for rule in self.rules:
            for condition in rule.conditions:
                if condition not in unique_conditions:
                    unique_conditions.append(condition)

        print(unique_conditions)