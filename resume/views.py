from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpRequest
from resume.models import Skill, SuperSkill, Education, Work
from resume.forms import EmailForm
from resume.utils import send_email
from django.views import View
from .py_scripts.secret_santa import get_santa_list

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
        return render(request, 'resume/education-tag.html')
class ShowWorkTag(View):

    def get(self, request: HttpRequest):
        works = Work.objects.order_by('-year_start', '-year_end')
        if works:
            return render(request, 'resume/work-tag.html', {'works': works})
        return render(request, 'resume/work-tag.html')


class ShowMusic(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/music.html')

class ShowMusicTag(View):

    def get(self, request: HttpRequest):
        return render(request, 'resume/music-tag.html')

class ShowEmail(View):

    def get(self, request: HttpRequest):
        form = EmailForm()
        return render(request, 'resume/email.html', {'form': form})
    
    def post(self, request: HttpRequest):
        form = EmailForm(request.POST)

        if form.is_valid():
            cleaned = form.cleaned_data
            email_sent = send_email(
                                cleaned.get('name'),
                                cleaned.get('email'),
                                cleaned.get('message'))
            

            return render(request, 'resume/email.html', {'form': form})
        else:
            print(form.errors)
            return render(request, 'resume/email.html')


class ShowEmailTag(View):
    def get(self, request: HttpRequest):
        form = EmailForm()
        return render(request, 'resume/email-tag.html', {'form': form})

class ShowSecretSanta(View):
    def get(self, request: HttpRequest):
        # return HttpResponse(santa_list)
        return render(request, 'resume/secret-santa.html')
    
    def post(self, request: HttpRequest):
        names = []
        # print(request.POST)
        for key, value in request.POST.items():
            if key.startswith('name'):
                nr = key[4:]
                mail = request.POST.get(f'mail{nr}')
                names.append((value, mail))

        santa_list = get_santa_list(names)

        for giver, receiver in santa_list:
            giver_name, giver_email = giver
            receiver_name = receiver[0]
            message = f"Leynivinur þinn er {receiver_name}"

            was_sent = send_email(giver_name, 'Secret Santa', message, giver_email)

        return render(request, 'resume/secret-santa.html', {'was_sent': was_sent})