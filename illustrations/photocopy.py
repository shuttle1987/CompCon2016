from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)


example_goal = Goal("Photocopy documents")

photocopy_skill = Skill("use\nphotocopier", KnowledgeState.KNOWN_AWARE)

example = KnowledgeHierachy("Photocopying example", nodes=[photocopy_skill, example_goal])
example.add_edge(photocopy_skill, example_goal, KnowledgeRelation.KNOWN_CONNECTION)
example.create_image()

