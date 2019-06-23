"""multidomainlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', 
        auth_views.LoginView.as_view(
            template_name='examplesite/login.html',
            redirect_authenticated_user=True,
        ),
        name='login'
    ),
    path('logout/', 
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('',
        login_required(TemplateView.as_view(template_name='examplesite/base.html')),
        name='home'
    ),
    path('other_domain/',
        xframe_options_exempt(TemplateView.as_view(template_name='examplesite/otherdomain.html')),
        name='other_domain',
    ),
]
