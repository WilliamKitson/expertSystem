from rule import Rule

class Expert:
    def __init__(self):
        self.__rules = []
        self.__facts = []

    def add_rule(self, conditions, conclusion):
        self.__rules.append(Rule(conditions, conclusion))

    def investigate(self):
        for unique_condition in self.__calculate_unique_conditions():
            for rule in self.__rules:
                if all(fact in self.__facts for fact in rule.conditions):
                    if not rule.incorrect:
                        if input(f"A: {rule.conclusion}? (yes/no): ") == 'yes':
                            return

                        else:
                            rule.incorrect = True

            if input(f"Q: {unique_condition}? (yes/no): ") == 'yes':
                self.__facts.append(unique_condition)

    def __calculate_unique_conditions(self):
        output = []

        for rule in self.__rules:
            for condition in rule.conditions:
                if condition not in output:
                    output.append(condition)

        return output

    def explain_conclusion(self):
        return f"facts: {self.__facts}"