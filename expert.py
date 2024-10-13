from rule import Rule
from question import Question

class Expert:
    def __init__(self):
        self.__rules = []
        self.__questions = []
        self.__conclusions = []

    def add_rule(self, conditions, conclusion):
        self.__rules.append(Rule(conditions, conclusion))

    def investigate(self):
        self.__calculate_questions()

        while not self.__conclusions:
            self.__ask_question()
            self.__process_facts()

    def __calculate_questions(self):
        for unique_condition in self.__calculate_unique_conditions():
            self.__questions.append(Question(unique_condition))

    def __calculate_unique_conditions(self):
        unique_conditions = []

        for condition in self.__collect_conditions():
            if condition not in unique_conditions:
                unique_conditions.append(condition)

        return unique_conditions

    def __collect_conditions(self):
        conditions = []

        for rule in self.__rules:
            for condition in rule.conditions:
                conditions.append(condition)

        return conditions

    def __ask_question(self):
        for question in self.__questions:
            if not question.asked:
                question.asked = True
                question.fact = input(f"Q: {question.question}? (yes/no): ") == "yes"
                return

    def __process_facts(self):
        for rule in self.__rules:
            if all(fact in self.__calculate_facts() for fact in rule.conditions):
                self.__conclusions.append(rule.conclusion)

    def __calculate_conclusions(self):
        conclusions = []

        for conclusion in self.__conclusions:
            conclusions.append(conclusion)

        return conclusions

    def __calculate_facts(self):
        facts = []

        for question in self.__questions:
            if question.fact:
                facts.append(question.question)

        return facts

    def get_conclusion(self):
        return f"conclusion: {self.__calculate_conclusions()}, facts: {self.__calculate_facts()}"