from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserProfileForm

from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        pass
       

def signup(request):
    
    registered = False
   
    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() :
           
            user = user_form.save(commit = True)
            registered = True
            return redirect('login')
            
    else:
        user_form = UserProfileForm()
    dic = {'title':'registration','registered':registered,'form':user_form,
            }
    return render(request,'userApp/signup.html',dic)

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = User.authenticate(email=email, password=raw_password)
#             User.login(request, user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'userApp/signup.html', {'form': form})