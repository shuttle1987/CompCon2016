from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)

single_page_web_apps = Goal("Create single page \n web apps")
websites = Goal("Create\nwebsites")
web_apis = Goal("Create\nweb APIs")
scalable_sites = Goal("Scalable services")


backend_language_fundamentals = Skill("Backend\nprogramming\nlanguage", KnowledgeState.KNOWN_AWARE)
backend_web_framework = Skill("Backend\nframework", KnowledgeState.KNOWN_AWARE)

automated_deployments = Skill("Automated\ndeployments", KnowledgeState.KNOWN_AWARE)
version_control = Skill("Version\ncontrol", KnowledgeState.KNOWN_AWARE)
javascript_skills = Skill("Javascript", KnowledgeState.KNOWN_AWARE)
frontend_framework = Skill("Frontend\nframework", KnowledgeState.KNOWN_AWARE)
css_skills = Skill("CSS skills", KnowledgeState.KNOWN_AWARE)
UI_UX_skills = Skill("UI/UX skills", KnowledgeState.KNOWN_AWARE)
industry_specific_skills = Skill("Known industry\nspecific skill", KnowledgeState.UNKNOWN_AWARE)
industry_specific_skills_unknown = Skill("Unknown\nindustry\nspecific skills\n(???)", KnowledgeState.UNKNOWN_UNAWARE)

web_dev_goals = [
    single_page_web_apps,
    websites,
    web_apis,
    scalable_sites,
]
web_dev_skills = [
    automated_deployments,
    backend_language_fundamentals,
    backend_web_framework,
    css_skills,
    frontend_framework,
    industry_specific_skills,
    industry_specific_skills_unknown,
    javascript_skills,
    UI_UX_skills,
    version_control,
]

web_dev_industry = KnowledgeHierachy("Web dev industry knowledge", nodes=web_dev_goals+web_dev_skills, rendering_engine='dot')

#Scalable goal
web_dev_industry.add_edge(version_control, automated_deployments, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(backend_language_fundamentals, automated_deployments, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(automated_deployments, scalable_sites, KnowledgeRelation.KNOWN_CONNECTION)

#Single page web apps goal
web_dev_industry.add_edge(backend_web_framework, single_page_web_apps, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(version_control, single_page_web_apps, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(UI_UX_skills, single_page_web_apps, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(css_skills, single_page_web_apps, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(javascript_skills, frontend_framework, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(frontend_framework, single_page_web_apps, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(industry_specific_skills, single_page_web_apps, KnowledgeRelation.KNOWN_CONNECTION)

#websites goal
web_dev_industry.add_edge(css_skills, websites, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(UI_UX_skills, websites, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(javascript_skills, websites, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(version_control, websites, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(industry_specific_skills, websites, KnowledgeRelation.KNOWN_CONNECTION)

#create web APIs doal
web_dev_industry.add_edge(backend_language_fundamentals, backend_web_framework, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(backend_web_framework, web_apis, KnowledgeRelation.KNOWN_CONNECTION)
web_dev_industry.add_edge(version_control, web_apis, KnowledgeRelation.KNOWN_CONNECTION)


web_dev_industry.create_image()
