from knowledge_hierachy.knowledge_hierachy  import KnowledgeHierachy, Goal, Skill

js_fundamentals = Skill("JS fundamentals")
python_fundamentals = Skill("python fundamentals")
django_skill = Skill("Django \n backend", "known")
frontend_skill = Skill("JS Frontend", "known")
mptt_skill = Skill("MPTT", "known")
d3_skill = Skill("D3", "known")
web_dev_2_nodes = [
    js_fundamentals,
    python_fundamentals,
    d3_skill,
    mptt_skill,
    backend_everything_skill,
    frontend_everything_skill,
    example_goal
]

web_project_actual = KnowledgeHierachy("Web development still too broad", nodes=web_dev_2_nodes)
#backend
web_project_actual.add_edge(python_fundamentals, django_skill, "known")
web_project_actual.add_edge(mptt_skill, django_skill, "known")
web_project_actual.add_edge(django_skill, example_goal, "known")

#frontend
web_project_actual.add_edge(js_fundamentals, frontend_skill, "known")
web_project_actual.add_edge(js_fundamentals, d3_skill, "known")
web_project_actual.add_edge(d3_skill, frontend_skill, "known")
web_project_actual.add_edge(frontend_skill, example_goal, "known")
web_project_actual.create_image()
