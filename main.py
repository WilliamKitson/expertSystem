from expert import Expert

expert = Expert()

expert.add_rule(["RPG", "Action", "Story Driven"], "Cyberpunk 2077")
expert.add_rule(["RPG", "Action", "Story Driven"], "Deus Ex")
expert.add_rule(["Survival Horror", "Classic", "Story Driven"], "Silent Hill 2")
expert.add_rule(["Comedy", "Story Driven", "Mystery", "Beat-Em-Up"], "Judgment")
expert.add_rule(["Comedy", "Story Driven", "Mystery", "Beat-Em-Up"], "Like a Dragon")
expert.investigate()

print(expert.get_conclusion())