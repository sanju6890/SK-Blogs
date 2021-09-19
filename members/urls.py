from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name="register"),
    path('edit-profile/',UserEditView.as_view(), name="edit-profile"),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),    
    path('password/',ChangePasswordView.as_view(template_name='registration/change_password.html'), name="change-password"),
    path('password-changed/',views.password_changed, name="password-changed"),
    path('<int:pk>/profile',ShowProfilePageView.as_view(), name="show-profile-page"),
    path('<int:pk>/edit-profile-page',EditProfilePageView.as_view(), name="edit-profile-page"),
    path('create-profile-page',CreateProfilePageView.as_view(), name="create-profile-page"),
]