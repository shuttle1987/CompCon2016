from knowledge_hierachy.knowledge_hierachy  import KnowledgeHierachy, Goal, Skill

example_goal = Goal("Create a complex single page web app")

webdev_everything_skill = Skill("web development \n skills", "known")

web_dev_too_broad1 = KnowledgeHierachy("Web development too broad", nodes=[webdev_everything_skill, example_goal])
web_dev_too_broad1.add_edge(webdev_everything_skill, example_goal, "known")
web_dev_too_broad1.create_image()


backend_everything_skill = Skill("Backend \n skills", "unknown")
frontend_everything_skill = Skill("Frontend \n skills", "unknown")
web_dev_2_nodes = [backend_everything_skill, frontend_everything_skill, example_goal]
web_dev_too_broad2 = KnowledgeHierachy("Web development still too broad", nodes=web_dev_2_nodes)
web_dev_too_broad2.add_edge(frontend_everything_skill, example_goal, "known")
web_dev_too_broad2.add_edge(backend_everything_skill, example_goal, "known")
web_dev_too_broad2.create_image()
