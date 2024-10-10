from rule import Rule
from question import Question

class Expert:
    def __init__(self):
        self.__rules = []
        self.__questions = []
        self.__has_conclusion = False

    def add_rule(self, conditions, conclusion):
        self.__rules.append(Rule(conditions, conclusion))

    def investigate(self):
        self.__calculate_questions()

        while not self.__has_conclusion:
            self.__ask_question()
            #self.__attempt_answer()

    def __calculate_questions(self):
        unique_conditions = []

        for rule in self.__rules:
            for condition in rule.conditions:
                if condition not in unique_conditions:
                    unique_conditions.append(condition)

        for unique_condition in unique_conditions:
            self.__questions.append(Question(unique_condition))

    def __ask_question(self):
        for question in self.__questions:
            if not question.asked:
                question.asked = True

                if input(f"A: {question.question}? (yes/no): ") != 'yes':
                    question.fact = True

                return

    def __attempt_answer(self):
        for rule in self.__rules:
            if all(fact in self.__questions for fact in rule.conditions):
                if not rule.incorrect:
                    if input(f"A: {rule.conclusion}? (yes/no): ") != 'yes':
                        rule.incorrect = True

                    else:
                        self.__has_conclusion = True


    def explain_conclusion(self):
        facts = ""

        for question in self.__questions:
            if question.fact:
                facts += f"{question.conclusion},"

        return f"facts: {facts}"