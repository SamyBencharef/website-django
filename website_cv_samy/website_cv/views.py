from django.shortcuts import render
from django.http import HttpResponse
from website_cv.models import ProfesionnalExperiences, PersonalInformation, Education, Skill, Hobbie
from .forms import ContactForm

# Create your views here.

def home(request):

    return HttpResponse("""
        <h1> Welcome on my currilicum website !</h1>
        <p>The advanced scripting module is amazing !</p>
    """)

def view_portfolio(request, id_project):

    return HttpResponse(
        "You asked to see the project n° {0} !".format(id_project)
    )

def view_profesionnalExperience(request):
    experiences = ProfesionnalExperiences.objects.all()
    personal_infos = PersonalInformation.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    hobbies = Hobbie.objects.all()

    """ FORM PART """
    form = ContactForm(request.POST or None)
    sendForm = False

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        topic = form.cleaned_data['topic']
        message = form.cleaned_data['message']
        forward = form.cleaned_data['forward']
        sendForm = True

    return render(request, 'website_cv/accueil.html',
                  {'personal_infos': personal_infos,
                   'experiences': experiences,
                   'educations': educations,
                   'skills': skills,
                   'hobbies': hobbies,
                   'form': form,
                   'sendForm': sendForm})
