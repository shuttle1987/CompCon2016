from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)
example_goal = Goal("Make a web app that can display tree based information")

webdev_everything_skill = Skill("web development\nskills", KnowledgeState.UNKNOWN_AWARE)

web_dev_too_broad1 = KnowledgeHierachy("Web development too broad", nodes=[webdev_everything_skill, example_goal])
web_dev_too_broad1.add_edge(webdev_everything_skill, example_goal, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_too_broad1.create_image()


backend_everything_skill = Skill("Backend \n skills", KnowledgeState.UNKNOWN_AWARE)
frontend_everything_skill = Skill("Frontend \n skills", KnowledgeState.UNKNOWN_AWARE)
web_dev_2_nodes = [backend_everything_skill, frontend_everything_skill, example_goal]
web_dev_too_broad2 = KnowledgeHierachy("Web development still too broad", nodes=web_dev_2_nodes)
web_dev_too_broad2.add_edge(frontend_everything_skill, example_goal, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_too_broad2.add_edge(backend_everything_skill, example_goal, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_too_broad2.create_image()
