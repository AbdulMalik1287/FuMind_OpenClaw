from erp_skill import ERPSkill
from mes_skill import MESSkill
from scada_skill import SCADASkill

class SkillRegistry:
    def __init__(self):
        self._skills = {}
        for skill_cls in [ERPSkill, MESSkill, SCADASkill]:
            skill = skill_cls()
            self._skills[skill.name] = skill
            print(f"[Registry] Registered skill: {skill.name} (format: {skill.source_id_format})")

    def get(self, name):
        return self._skills.get(name)

    def list_skills(self):
        return list(self._skills.keys())