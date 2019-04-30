from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmailForm, CommentaryForm
from django.core.mail import send_mail, BadHeaderError
# Model import
from website_cv.models import ProfesionnalExperiences, PersonalInformation, Education, Skill, Hobbie, Commentary


# Create your views here.
def view_index(request):

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
