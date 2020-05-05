from django.contrib import messages
from django.shortcuts import render
from .models import *
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.shortcuts import reverse
from orgApp import forms
from userApp.models import UserProfile
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    
    total_org_list = Organisation.objects.filter(status=True).count()
    divisions = City.objects.all().order_by('name')
    districts = District.objects.all().order_by('name')
    thanas = Thana.objects.all().order_by('name')
    context = {}
    if total_org_list > 0:
        all_org = Organisation.objects.filter(status=True).order_by('name')
        paginator = Paginator(all_org, 1) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        all_org_page_obj = paginator.get_page(page_number)
    else:
        all_org = False
    
    context = {
        'organisation_list': all_org_page_obj,
        'divisions': divisions,
        'districts': districts,
        'thanas': thanas,
        'nbar': 'home',
    }
    return render(request, 'index_main.html', context)

@login_required
def organizationProfile(request):
    user = request.user
    total_org_list = Organisation.objects.all().count()
    context = {}
    profile_have = False
    if total_org_list > 0:
        org= Organisation.objects.filter(owner=user)
        profile_have = True
        context = {
            'profile_have': profile_have,
            'org_profile': org,
        }
    else: 
        context = {
            'profile_have': profile_have,
        }
    
    return render(request, 'orgApp/selfOrg.html',context=context)
    

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

def load_city(request):
    city = City.objects.all().order_by('name')
    return render(request, 'orgApp/city_dropdown_list_options.html', {'divisions': city})

def load_district(request):
    division_id = request.GET.get('city')
    
    districts = District.objects.filter(city=division_id).order_by('name')
    return render(request, 'orgApp/district_dropdown_list_options.html', {'districts': districts})

def load_thana(request):
    district_id = request.GET.get('district')
    
    thana = Thana.objects.filter(district=district_id).order_by('name')
    print(thana)
    return render(request, 'orgApp/thana_dropdown_list_options.html', {'thana': thana})

def org_project_create_view(request: HttpRequest):
    template_name = "orgApp/org_project_create.html"
    if request.method == 'GET':
        project_main_form = forms.OrgProjectMainRegForm()
        context = {'form': project_main_form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        project_main_form = forms.OrgProjectMainRegForm(data=request.POST)
        if project_main_form.is_valid():
            project_main_form.save()
            messages.add_message(request, messages.SUCCESS, "Project added successfully!!")
        else:
            messages.add_message(request, messages.ERROR, "Please correct those errors!!")
        return HttpResponsePermanentRedirect(reverse('orgApplication:org-project-create'))

