from expert import Expert

expert = Expert()

expert.add_rule(["RPG", "Action", "Story Driven"], "Cyberpunk 2077")
expert.add_rule(["Survival Horror", "Classic", "Story Driven"], "Silent Hill 2")
expert.investigate()