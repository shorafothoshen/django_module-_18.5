from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
def Registation(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            reg_form=forms.RegistationForm(request.POST)
            if reg_form.is_valid():
                messages.success(request, "Your Account is Create Successfully!!")
                reg_form.save()
                return redirect("LogIn_page")
            else:
                messages.warning(request,"Incorrect Informetions ❌")
                return redirect("registations_page")
        else:
            reg_form=forms.RegistationForm()
        return render(request,"Author/Registations.html",{"form":reg_form,"type":"Registation"})
    else:
        redirect("profile_page")


def LogIn(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            logIn_form=AuthenticationForm(request=request, data=request.POST)
            if logIn_form.is_valid():
                user_name=logIn_form.cleaned_data["username"]
                user_pass=logIn_form.cleaned_data["password"]
                print(user_name,user_pass)
                user=authenticate(username=user_name,password=user_pass)
                if user is not None:
                    messages.success(request,"LogIn Successfully✅")
                    login(request,user)
                    return redirect("profile_page")
            else:
                messages.warning(request, "Please Give your correct information❌")
                return redirect("LogIn_page")
        else:
            logIn_form=AuthenticationForm()
        return render(request,"Author/LogIn.html",{"form":logIn_form,"type":"Log-In"})
    else:
        redirect("profile_page")

@login_required
def Profile(request):
    return render(request,"Author/Profile.html",{"first":request.user.first_name,"last":request.user.last_name})

@login_required
def Edit_profile(request):
    if request.method=="POST":
        edit_form=forms.ChangeInfo(request.POST,instance=request.user)
        if edit_form.is_valid():
            messages.success(request,"Update Successfully✅")
            edit_form.save()
            return redirect("edit_page")
    else:
        edit_form=forms.ChangeInfo(instance=request.user)
    return render(request,"Author/info_change.html",{"form":edit_form,"type":"Edit-Profile"})

@login_required
def change_password(request):
    if request.method=="POST":
        pass_form=PasswordChangeForm(request.user,data=request.POST)
        if pass_form.is_valid():
            messages.success(request,"Password Update Successfully✅")
            pass_form.save()
            update_session_auth_hash(request, request.user)
            return redirect("edit_page")
        else:
            messages.warning(request,"Incorrect Information❌")
            return redirect("change_pass")
    else:
        pass_form=PasswordChangeForm(request.user)
    return render(request,"Author/pass_change.html",{"form":pass_form ,"type":"Change-password"})

@login_required
def Without_old_pass(request):
    if request.method=="POST":
        woPass_form=SetPasswordForm(request.user,data=request.POST)
        if woPass_form.is_valid():
            messages.success(request,"Password Update Successfully✅")
            woPass_form.save()
            update_session_auth_hash(request,request.user)
            return redirect("edit_page")
    else:
        woPass_form=SetPasswordForm(request.user)
    return render(request,"Author/wo_pass_change.html",{"form":woPass_form,"type":"Change-Password"})

def LogOut(request):
    logout(request)
    messages.success(request,"LogOut Successfully✅")
    return redirect("Home_page")