from rule import Rule

class Expert:
    def __init__(self):
        self.rules = []

    def add_rule(self, conditions, conclusion):
        self.rules.append(Rule(conditions, conclusion))

    def investigate(self):
        for rule in self.rules:
            print(rule.conclusion)