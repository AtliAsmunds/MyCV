from django import template
from resume.forms import EmailForm
from resume.models import Skill, SuperSkill, Education, Work

register = template.Library()

@register.inclusion_tag('resume/subskills.html')
def get_subskills(super_id):
    superskill: SuperSkill = SuperSkill.objects.get(id=super_id)
    if superskill:
        subskills = Skill.objects.filter(superskill=superskill).order_by('-level')

        if subskills:
            return {'subskills': subskills}

@register.inclusion_tag('resume/about-tag.html')
def get_about_page():
    return {}

@register.inclusion_tag('resume/education-tag.html')
def get_education():
    degrees = Education.objects.order_by('-year_start', '-year_end')
    if degrees:
        return {'degrees': degrees}

@register.inclusion_tag('resume/work-tag.html')
def get_work():
    works = Work.objects.order_by('-year_start', '-year_end')
    if works:
        return {'works': works}

@register.inclusion_tag('resume/skills-tag.html')
def get_skills():
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
    
    return context
@register.inclusion_tag('resume/music-tag.html')
def get_music():
    return {}

@register.inclusion_tag('resume/email-tag.html')
def get_email(form: EmailForm):
    return {'form': form, 'posted': form.is_bound}