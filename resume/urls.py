from django.urls import path
from resume import views

app_name = 'resume'

urlpatterns = [
  path('', views.ShowAbout.as_view(), name='index'),
  path('about/', views.ShowAbout.as_view(), name='about'),
  path("about-tag/", views.ShowAboutTag.as_view(), name='about-tag'),
  path("education-tag/", views.ShowEducationTag.as_view(), name='education-tag'),
  path("work-tag/", views.ShowWorkTag.as_view(), name='work-tag'),
  path('education/', views.ShowEducation.as_view(), name='education'),
  path("work/", views.ShowWork.as_view(), name="work"),
  path('skills/', views.ShowSkills.as_view(), name="skills"),
  path('skills-tag/', views.ShowSkillsTag.as_view(), name="skills-tag"),
  path("music/", views.ShowMusic.as_view(), name="music"),
  path("music-tag/", views.ShowMusicTag.as_view(), name="music-tag"),
  path("email/", views.ShowEmail.as_view(), name="email"),
  path("email-tag/", views.ShowEmailTag.as_view(), name="email-tag"),
  path("secret-santa/", views.ShowSecretSanta.as_view(), name="secret-santa")
]
