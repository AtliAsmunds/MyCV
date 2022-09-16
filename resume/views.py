from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from resume.models import Skill, SuperSkill, Education, Work
from django.views import View

# Create your views here.
class ShowSkills(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/skills.html')

class ShowSkillsTag(View):

    def get(self, request: HttpRequest):
        context = {}
        superskills = SuperSkill.objects.order_by('-level')

        if superskills:
            context['skills'] = []
            for superskill in superskills:
                subskills = Skill.objects.filter(superskill=superskill).order_by('-level')

                if subskills:
                    context['skills'].append({
                        'superskill': superskill,
                        'subskills': subskills
                    })
        
        return render(request, 'resume/skills-tag.html', context)

class ShowAbout(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/about.html')

class ShowEducation(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/education.html')

class ShowWork(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/work.html')

class ShowAboutTag(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/about-tag.html')

class ShowEducationTag(View):

    def get(self, request: HttpRequest):
        degrees = Education.objects.order_by('-year_start', '-year_end')
        if degrees:
            return render(request, 'resume/education-tag.html', {'degrees': degrees})
class ShowWorkTag(View):

    def get(self, request: HttpRequest):
        works = Work.objects.order_by('-year_start', '-year_end')
        if works:
            return render(request, 'resume/work-tag.html', {'works': works})


class ShowMusic(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/music.html')

class ShowMusicTag(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/music-tag.html')