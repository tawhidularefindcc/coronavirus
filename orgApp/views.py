from django.shortcuts import render
from .models import *
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.shortcuts import reverse
from orgApp import forms
from userApp.models import UserProfile
from .models import Organisation
from django.contrib.auth.decorators import login_required



# Create your views here.
def test(request):
    return render(request, 'index_main.html', {'nbar': 'home'})


def home(request):
    context = {
        'Organisations': Organisation.objects.all()
    }
    return render(request, 'orgApp/home.html', context)

@login_required
def self_org(request: HttpRequest):
    logged_in_user = request.user
    # user = UserProfile.objects.all()[:1].get()
    queryset = Organisation.objects.filter()
    # new = True if queryset.count() == 0 else None
    new = True
    context = {'queryset': queryset, 'errorMsg': None, 'new': new}

    # check for request type
    context['nbar'] = 'org_reg'
    if request.method == 'GET':
        if new:
            form = forms.OrganisationMainRegForm()
            org_detail_form = forms.OrgDetailMainRegForm()

            context['orgForm'] = form
            context['org_detail_form'] = org_detail_form
        return render(request, 'orgApp/selfOrg.html', context)
    elif request.method == 'POST':
        if new:
            form = forms.OrganisationMainRegForm(request.POST,request.FILES)
            orgForm = forms.OrgDetailMainRegForm(request.POST, request.FILES)
            if form.is_valid() and orgForm.is_valid():
                new_org = form.save(commit = False)
                new_org.owner = logged_in_user
                new_org = form.save(commit = True)
                details = orgForm.save(commit=False)
                details.organisation = new_org
                details.save()
                return HttpResponsePermanentRedirect(reverse("orgApplication:self_org"))
        context['errorMsg'] = 'Not new user'
        return render(request, 'orgApp/selfOrg.html', context)
