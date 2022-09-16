from django.test import TestCase
from resume.models import Skill

# Create your tests here.

class SkillModelTests(TestCase):

    def test_skill_level_not_below_zero(self):
        skill = Skill(name="New Skill", level=-1)
        skill.save()

        self.assertEqual((skill.level >= 0), True)
    
    def test_skill_level_not_above_five(self):
        skill = Skill(name="New Skill", level=6)
        skill.save()

        self.assertEqual((skill.level <= 5), True)
    
    def test_superskill_is_reachable(self):
        superskill = Skill('Super', level=4)
        skill = Skill('Subskill', level=3, superskill=superskill)

        self.assertEqual(skill.superskill.name, superskill.name)