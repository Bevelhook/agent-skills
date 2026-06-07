# skills/skill_greet.py

class SkillGreet:
    def __init__(self):
        self.name = "Greet Skill"

    def execute(self, name="User"):
        return f"Welcome, {name}!"