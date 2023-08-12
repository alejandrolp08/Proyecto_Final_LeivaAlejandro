from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "CORE"

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="CORE/logout.html"), name="logout"),
    path('about/', TemplateView.as_view(template_name="CORE/about.html"), name="about"),
    path('register/', views.register, name="register"),
    path('editprofile/', views.editProfile, name="editProfile"),
]

urlpatterns += staticfiles_urlpatterns()