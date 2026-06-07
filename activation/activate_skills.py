# activation/activate_skills.py

import importlib
import os

def load_skills():
    skills_dir = "skills"
    skills = []

    for file in os.listdir(skills_dir):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = importlib.import_module(f"{skills_dir}.{module_name}")
            skill_class = getattr(module, module_name.capitalize())
            skills.append(skill_class())
    return skills

def activate_skills():
    skills = load_skills()
    print("Activating skills...")
    for skill in skills:
        print(f"Executing {skill.name}:")
        if skill.name == "Greet Skill":
            print(skill.execute("Bevelhook"))
        else:
            print(skill.execute())

if __name__ == "__main__":
    activate_skills()