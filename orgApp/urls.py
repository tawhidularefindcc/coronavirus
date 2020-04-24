from django.urls import path


from . import views

app_name = "orgApplication"

urlpatterns = [
    path('', views.test, name='org'),
    path("reg/", views.self_org, name='self_org'),
    
]
