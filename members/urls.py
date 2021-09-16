from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name="register"),
    path('edit-profile/',UserEditView.as_view(), name="edit-profile"),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),    
    path('password/',ChangePasswordView.as_view(template_name='registration/change_password.html'), name="change-password"),
    path('password-changed/',views.password_changed, name="password-changed")
]