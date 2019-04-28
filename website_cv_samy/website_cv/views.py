from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmailForm, CommentaryForm

# Model import
from website_cv.models import ProfesionnalExperiences, PersonalInformation, Education, Skill, Hobbie, Commentary

# Form import
# from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

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
    commentaries = Commentary.objects.filter(visible=True)

    sendFormEmail = False
    sendFormCommentary = False

    if request.method == 'POST':
        formEmail = EmailForm(request.POST)
        formCommentary = CommentaryForm(request.POST)
        if formEmail.is_valid():
            name = formEmail.cleaned_data['name']
            email = formEmail.cleaned_data['email']
            topic = formEmail.cleaned_data['topic']
            message = formEmail.cleaned_data['message']
            emailSender = name + " " + email

            formEmail.save()
            sendFormEmail = True
            try:
                send_mail(topic, message, emailSender, ['samybencharef@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        if formCommentary.is_valid():
            formCommentary.save()
            sendFormCommentary = True
    else:
        formEmail = EmailForm()
        formCommentary = CommentaryForm()

    return render(request, 'website_cv/accueil.html',
                  {'personal_infos': personal_infos,
                   'experiences': experiences,
                   'educations': educations,
                   'skills': skills,
                   'hobbies': hobbies,
                   'commentaries': commentaries,
                   'formEmail': formEmail,
                   'sendFormEmail': sendFormEmail,
                   'formCommentary': formCommentary,
                   'sendFormCommentary': sendFormCommentary
                   })
