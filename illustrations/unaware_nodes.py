
from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Skill,
    KnowledgeState,
)


known_skill_unaware = Skill("Known skill\n (Unaware)", KnowledgeState.KNOWN_UNAWARE)
unknown_skill_unaware = Skill("Unknown skill\n (Unaware)", KnowledgeState.UNKNOWN_UNAWARE)

skill_type_nodes = [
    known_skill_unaware, 
    unknown_skill_unaware, 
]

legend = KnowledgeHierachy("Unaware nodes", nodes=skill_type_nodes)
legend.create_image()
