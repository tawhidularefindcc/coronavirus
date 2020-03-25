from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings


# Create your views here.

def index(request):
    return render(request,'index.html')


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            if name and message and email:
                msg = 'Name : '+name + '\nEmail : ' + email + '\nMessage : '+message

                try:
                    send_mail(name, msg, email, ['jubel8180@gmail.com'],fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, "index.html",{'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')