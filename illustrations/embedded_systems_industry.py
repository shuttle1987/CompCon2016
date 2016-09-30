from knowledge_hierachy.knowledge_hierachy import (
    KnowledgeHierachy,
    Goal,
    Skill,
    KnowledgeState,
    KnowledgeRelation,
)

microcontroller_firmware = Goal("Create microcontroller\nbased produtcs", KnowledgeState.KNOWN_AWARE)
embedded_linux= Goal("Create embedded\nlinux products", KnowledgeState.KNOWN_AWARE)

systems_programming_skills = Skill("Systems\nprogramming", KnowledgeState.KNOWN_AWARE)
assembly_programming_skill = Skill("Assembly\nprogramming", KnowledgeState.KNOWN_AWARE)
low_level_programming_skill = Skill("Low-level\nprogramming", KnowledgeState.KNOWN_AWARE)


memory_management_skills = Skill("Resource\nmanagement", KnowledgeState.KNOWN_AWARE)
version_control = Skill("Version\ncontrol", KnowledgeState.KNOWN_AWARE)
build_systems = Skill("Build\nsystems", KnowledgeState.KNOWN_AWARE)
driver_skills = Skill("Writing device\ndrivers", KnowledgeState.KNOWN_AWARE)


electronics_skills = Skill("Electronics\nskills", KnowledgeState.KNOWN_AWARE)
fpga_skills = Skill("FPGA", KnowledgeState.KNOWN_AWARE)

industry_specific_skills = Skill("Known industry\nspecific skill", KnowledgeState.UNKNOWN_AWARE)
industry_specific_skills_unknown = Skill("Unknown industry\nspecific skills\n(???)", KnowledgeState.UNKNOWN_UNAWARE)

embedded_goals = [
    microcontroller_firmware,
    embedded_linux,
]

embedded_skills = [
    assembly_programming_skill,
    driver_skills,
    electronics_skills,
    fpga_skills,
    industry_specific_skills,
    industry_specific_skills_unknown,
    low_level_programming_skill,
    memory_management_skills,
    systems_programming_skills,
    version_control,
]

embedded_nodes = embedded_goals + embedded_skills
embedded_industry = KnowledgeHierachy(
    "Embedded systems industry knowledge",
    nodes=embedded_nodes
)

#systems programming
embedded_industry.add_edge(low_level_programming_skill, systems_programming_skills, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(memory_management_skills, systems_programming_skills, KnowledgeRelation.KNOWN_CONNECTION)

#microcontroller firmware goal
embedded_industry.add_edge(industry_specific_skills, microcontroller_firmware, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(systems_programming_skills, microcontroller_firmware, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(version_control, microcontroller_firmware, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(build_systems, microcontroller_firmware, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(low_level_programming_skill, microcontroller_firmware, KnowledgeRelation.KNOWN_CONNECTION)

#embedded linux
embedded_industry.add_edge(industry_specific_skills, embedded_linux, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(driver_skills, embedded_linux, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(systems_programming_skills, embedded_linux, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(low_level_programming_skill, embedded_linux, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(version_control, embedded_linux, KnowledgeRelation.KNOWN_CONNECTION)
embedded_industry.add_edge(build_systems, embedded_linux, KnowledgeRelation.KNOWN_CONNECTION)


embedded_industry.create_image()
