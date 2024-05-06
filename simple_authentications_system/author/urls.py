from django.urls import path
from . import views
urlpatterns = [
    path("registation/",views.Registation,name="registations_page"),
    path("profile/",views.Profile,name="profile_page"),
    path("logIn/",views.LogIn,name="LogIn_page"),
    path("profile/edit/",views.Edit_profile,name="edit_page"),
    path("profile/edit/password_change/",views.change_password,name="change_pass"),
    path("profile/edit/change_password/",views.Without_old_pass,name="pass_change"),
    path("logout/",views.LogOut,name="Logout_page"),
]
