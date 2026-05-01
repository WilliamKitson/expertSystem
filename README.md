# Expert System

Small Python expert system that uses hand-written rules to recommend games based on yes/no answers.

## What It Does

The project builds a simple rule engine:

- `Rule` stores a list of required conditions and a conclusion.
- `Question` tracks whether a condition has been asked and whether the answer was `yes`.
- `Expert` collects all unique conditions from the rules, asks the user about them, and adds conclusions when a rule's conditions are satisfied.

The sample dataset in [`main.py`](/Users/williamkitson/PyCharmProjects/expertSystem/main.py) recommends:

- `Cyberpunk 2077`
- `Deus Ex`
- `Silent Hill 2`
- `Judgment`
- `Like a Dragon`

## Project Layout

- [`main.py`](/Users/williamkitson/PyCharmProjects/expertSystem/main.py): entry point and example knowledge base
- [`expert.py`](/Users/williamkitson/PyCharmProjects/expertSystem/expert.py): rule evaluation and question loop
- [`rule.py`](/Users/williamkitson/PyCharmProjects/expertSystem/rule.py): rule model
- [`question.py`](/Users/williamkitson/PyCharmProjects/expertSystem/question.py): question model

## Requirements

- Python 3

No third-party packages are used.

## Run

```bash
python3 main.py
```

You will be prompted with questions like:

```text
Q: RPG? (yes/no):
```

Answer with `yes` or `no`.

## Example

If you answer `yes` to `RPG`, `Action`, and `Story Driven`, the program returns:

```text
conclusion: ['Cyberpunk 2077', 'Deus Ex'], facts: ['RPG', 'Action', 'Story Driven']
```

## How Rules Are Added

Rules are defined in `main.py` with:

```python
expert.add_rule(["RPG", "Action", "Story Driven"], "Cyberpunk 2077")
```

The first argument is the list of required facts. The second argument is the conclusion produced when all facts are true.

## Current Limitation

The investigation loop stops only when at least one conclusion is found. If the user answers in a way that matches no rule, the program can get stuck after all questions have been asked because there is no fallback or "no match" exit path yet.
