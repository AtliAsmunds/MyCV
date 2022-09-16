import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_webpage_project.settings')

import django
django.setup()
from resume.models import Skill, SuperSkill

def populate():
    py_skills = [
        {'name': 'nltk', 'level': 3},
        {'name': 'spacy', 'level': 3},
        {'name': 'pandas', 'level': 3},
        {'name': 'django', 'level': 4}
    ]

    web_skills = [
        {'name': 'html', 'level': 5},
        {'name': 'css', 'level': 4},
        {'name': 'javascript', 'level': 3},
        {'name': 'typescript', 'level': 3},
        {'name': 'node.js', 'level': 3}
    ]

    cloud_skills = [
        {'name': 'AWS', 'level': 2},
        {'name': 'Azure', 'level': 1}
    ]

    others = [
        {'name': 'linux', 'level': 4},
        {'name': 'bash', 'level': 4},
        {'name': 'VScode', 'level': 4}
    ]

    superskills = [
        {'name': 'Python', 'level': 5, 'subskills': py_skills},
        {'name': 'WebDev', 'level': 4, 'subskills': web_skills},
        {'name': 'Cloud', 'level': None, 'subskills': cloud_skills},
        {'name': 'Other', 'level': None, 'subskills': others}
    ]

    for s in superskills:
        superskill: SuperSkill = add_superskill(s)
        for subs in s['subskills']:
            add_subskill(subs, superskill)

    for ss in SuperSkill.objects.all():
        for s in Skill.objects.filter(superskill=ss):
            print(f"- {ss}: {s}")

def add_superskill(data: dict) -> SuperSkill:
    skill: SuperSkill = SuperSkill.objects.get_or_create(
        name=data['name'],
        level=data['level']
    )[0]

    skill.save()
    return skill

def add_subskill(data:dict, superskill: SuperSkill) -> Skill:
    skill: Skill = Skill.objects.get_or_create(
        name=data['name'],
        level=data['level'],
        superskill=superskill
    )[0]

    skill.save()
    return skill


if __name__ == "__main__":
    print("Populating database")
    populate()