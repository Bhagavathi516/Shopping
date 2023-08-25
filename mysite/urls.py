"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.forms import UserLoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_view/', user_views.superuser_view, name='admin_view'),
    path('signup/', user_views.user_signup_view, name='register'),
    path('profile/', user_views.user_profile_view, name='profile'),
    # path('login/', auth_views.LoginView.as_view(authentication_form=UserLoginForm, template_name='users/login.html'), name='login'),
    path('login/', user_views.user_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_change/', user_views.CustomPasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    # path('password-reset/', 
    #     auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
    #     name='password_reset'),
    # path('password-reset/done/', 
    #     auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
    #     name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', 
    #     auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    #     name='password_reset_confirm'),
    path('', include('shopping.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
