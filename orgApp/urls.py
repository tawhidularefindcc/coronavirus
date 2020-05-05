from django.urls import path


from . import views

app_name = "orgApplication"

urlpatterns = [
    path('', views.home, name='org'),
    path("reg/", views.self_org, name='self_org'),
    path("org-profile/", views.organizationProfile, name='org_profile'),
    path("org-project-create/", views.org_project_create_view, name='org-project-create'),
    path('ajax/load-districts/', views.load_district, name='ajax_load_districts'),
    path('ajax/load-thanas/', views.load_thana, name='ajax_load_thana'),
    path('ajax/load-divisions/', views.load_thana, name='ajax_load_division'),
]