from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)

goal = Goal("Goal")

known_skill = Skill("Known skill\n (Aware)", KnowledgeState.KNOWN_AWARE)
known_skill_unaware = Skill("Known skill\n(unaware)", KnowledgeState.KNOWN_UNAWARE)

unknown_skill_aware = Skill("Unknown skill\n (Aware)", KnowledgeState.UNKNOWN_AWARE)
unknown_skill_unaware = Skill("Unknown skill\n (Unaware)", KnowledgeState.UNKNOWN_UNAWARE)

goal_nodes = [goal]
skill_type_nodes = [
    known_skill,
    known_skill_unaware,
    unknown_skill_aware, 
    unknown_skill_unaware, 
]

legend = KnowledgeHierachy("legend", nodes=goal_nodes+skill_type_nodes)
legend.create_image()
