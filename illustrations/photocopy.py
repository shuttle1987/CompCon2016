from knowledge_hierachy.knowledge_hierachy  import KnowledgeHierachy, Goal, Skill


example_goal = Goal("Photocopy documents")

photocopy_skill = Skill("use \n photocopier", "known")

example = KnowledgeHierachy("Photocopying example", nodes=[photocopy_skill, example_goal])
example.add_edge(photocopy_skill, example_goal, "known")
example.create_image()

