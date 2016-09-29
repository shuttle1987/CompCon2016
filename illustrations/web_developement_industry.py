from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)

single_page_web_apps = Goal("Create single page \n web apps")
web_apis = Goal("Create web APIs")
scalable_sites = Goal("Scalable services")


backend_language_fundamentals = Skill("Backend\nprogramming language", KnowledgeState.KNOWN_AWARE)

automated_deployments = Skill("Automated deployments", KnowledgeState.KNOWN_AWARE)
version_control = Skill("Version control", KnowledgeState.KNOWN_AWARE)
industry_specific_skills = Skill("Known industry\nspecific skill", KnowledgeState.UNKNOWN_AWARE)
industry_specific_skills_unknown = Skill("Unknown industry\nspecific skills (???)", KnowledgeState.UNKNOWN_UNAWARE)

web_dev_insdutry_nodes = [
    single_page_web_apps,
    web_apis,
    scalable_sites,
    backend_language_fundamentals,
    automated_deployments,
    version_control,
    industry_specific_skills,
    industry_specific_skills_unknown,
]

web_dev_industry = KnowledgeHierachy("Web dev industry knowledge", nodes=web_dev_insdutry_nodes, rendering_engine='neato')


web_dev_industry.create_image()
