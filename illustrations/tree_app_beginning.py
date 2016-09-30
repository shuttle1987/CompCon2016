from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)

web_app_goal = Goal("Make a web app that can display tree based information")

js_fundamentals = Skill("Javascript\nfundamentals", KnowledgeState.KNOWN_AWARE)
python_fundamentals = Skill("Python\nfundamentals", KnowledgeState.KNOWN_AWARE)
django_skill = Skill("Django\nbackend", KnowledgeState.KNOWN_AWARE)
frontend_skill = Skill("JS Frontend", KnowledgeState.KNOWN_AWARE)
mptt_skill = Skill("Store trees\nefficiently in\nrelational DB\n???", KnowledgeState.UNKNOWN_UNAWARE)
d3_skill = Skill("JS tree view\nlibrary???", KnowledgeState.UNKNOWN_AWARE)
REST_api_skill = Skill("REST\nAPI", KnowledgeState.KNOWN_AWARE)
web_dev_2_nodes = [
    js_fundamentals,
    python_fundamentals,
    d3_skill,
    mptt_skill,
    django_skill,
    frontend_skill,
    REST_api_skill,
    web_app_goal
]

web_project_actual = KnowledgeHierachy("TreeVis beginning of project", nodes=web_dev_2_nodes)
#backend
web_project_actual.add_edge(python_fundamentals, django_skill, KnowledgeRelation.KNOWN_CONNECTION)
web_project_actual.add_edge(mptt_skill, django_skill, KnowledgeRelation.UNKNOWN_CONNECTION)
web_project_actual.add_edge(django_skill, web_app_goal, KnowledgeRelation.KNOWN_CONNECTION)

#frontend
web_project_actual.add_edge(js_fundamentals, frontend_skill, KnowledgeRelation.KNOWN_CONNECTION)
web_project_actual.add_edge(js_fundamentals, d3_skill, KnowledgeRelation.KNOWN_CONNECTION)
web_project_actual.add_edge(d3_skill, frontend_skill, KnowledgeRelation.KNOWN_CONNECTION)
web_project_actual.add_edge(frontend_skill, web_app_goal, KnowledgeRelation.KNOWN_CONNECTION)

#both frontend and backend
web_project_actual.add_edge(REST_api_skill, frontend_skill, KnowledgeRelation.KNOWN_CONNECTION)
web_project_actual.add_edge(REST_api_skill, django_skill, KnowledgeRelation.KNOWN_CONNECTION)


web_project_actual.create_image()
