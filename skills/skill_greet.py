def activate_skills():
    skills = load_skills()
    print("Activating skills...\n")
    
    for skill in skills:
        try:
            print(f"→ Running {skill.name}")
            if hasattr(skill, 'execute'):
                result = skill.execute() if skill.name != "Greet Skill" else skill.execute("Bevelhook")
                print(f"  Result: {result}\n")
            else:
                print(f"  No execute() method found\n")
        except Exception as e:
            print(f"  Failed: {e}\n")# skills/skill_greet.py

class SkillGreet:
    def __init__(self):
        self.name = "Greet Skill"

    def execute(self, name="User"):
        return f"Welcome, {name}!"