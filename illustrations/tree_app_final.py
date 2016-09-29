from knowledge_hierachy.knowledge_hierachy  import KnowledgeHierachy, Goal, Skill

web_app_goal = Goal("Make a web app that can display tree based information")

js_fundamentals = Skill("Javascript \n  fundamentals", "known")
python_fundamentals = Skill("Python \n fundamentals", "known")
django_skill = Skill("Django \n backend", "known")
frontend_skill = Skill("JS Frontend", "known")
mptt_skill = Skill("MPTT", "unknown")
d3_skill = Skill("D3 library", "known")
REST_api_skill = Skill("REST\nAPI", "known")
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

web_project_actual = KnowledgeHierachy("TreeVis end of project", nodes=web_dev_2_nodes)
#backend
web_project_actual.add_edge(python_fundamentals, django_skill, "known")
web_project_actual.add_edge(mptt_skill, django_skill, "known")
web_project_actual.add_edge(django_skill, web_app_goal, "known")

#frontend
web_project_actual.add_edge(js_fundamentals, frontend_skill, "known")
web_project_actual.add_edge(js_fundamentals, d3_skill, "known")
web_project_actual.add_edge(d3_skill, frontend_skill, "known")
web_project_actual.add_edge(frontend_skill, web_app_goal, "known")

#both frontend and backend
web_project_actual.add_edge(REST_api_skill, frontend_skill, "known")
web_project_actual.add_edge(REST_api_skill, django_skill, "known")


web_project_actual.create_image()
