from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, DetailView, UpdateView
from django.utils import translation
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . import forms
from . import models,mixins



class LoginView(mixins.LoggedOutOnlyView,FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm


    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
           # messages.success(self.request, f"welcome back {user.first_name}")
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")
def log_out(request):
    logout(request)
    messages.info(request, "به امید دیدار")
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")


    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)



# def github_login(request):
#     client_id = 'Ov23liqSXx17wD1siIpm'
#     redirect_uri = 'http://127.0.0.1:8000/users/login/github/callback'
#     return redirect(f"http://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user")
#
#
# class GithubException(Exception):
#     pass
#
# def github_callback(request):
#     try:
#         client_id = 'Ov23liqSXx17wD1siIpm'
#         client_secret = '17b75f28681b4e17d3863417f4486f595b2e2012'
#         code = request.GET.get("code",None)
#         if code is None:
#             result = requests.post(f"http://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
#                 headers={"Accept": "application/json"})
#             result_json = result.json()
#             error = result_json.get("error",None)
#             if error is not None:
#                 raise GithubException()
#             else:
#                 access_token = result_json.get("access_token")
#                 profile_request = requests.get("https://api.github.com/user",headers={"Authorization":f"token {access_token}", "Accept": "application/json",})
#                 profile_json = profile_request.json()
#                 username = profile_json.get("login",None)
#                 if username is not None:
#                     name = profile_json.get("name")
#                     email = profile_json.get("email")
#                     bio = profile_json.get("bio")
#                     try:
#                         user = models.User.objects.get(email=email)
#                         if user.login_method != models.User.LOGIN_GITHUB:
#                             raise GithubException()
#                     except models.User.DoesNotExist:
#                         user = models.User.objects.create(email=email,first_name=name,username=email,bio=bio,login_method=models.User.LOGIN_GITHUB)
#                         user.set_unusable_password()
#                         user.save()
#                     login(request,user)
#                     return redirect(reverse("core:home"))
#
#                 else:
#                     raise GithubException()
#         else:
#             raise GithubException()
#     except GithubException:
#         return redirect(reverse("users:login"))

class UserProfileView(DetailView):
    model = models.User
    context_object_name = "user_obj"

class UpdateProfileView(mixins.LoggedInOnlyView,SuccessMessageMixin, UpdateView):
    model = models.User

    template_name = "users/update-profile.html"
    fields = (

        "first_name",
        "last_name",
        "birthdate",
        "gender",
        "bio",
        "language",
        "currency",
        "avatar",

    )
    success_message = "پروفایل تغییر یافت"
    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class = form_class)
        form.fields["birthdate"].widget.attrs = {
            "placeholder": "تاریخ تولد",
            "style": "text-align: right;"
        }
        form.fields["first_name"].widget.attrs = {
            "placeholder": "نام",
            "style": "text-align: right;"
        }
        form.fields["last_name"].widget.attrs = {
            "placeholder": "نام خانوادگی",
            "style": "text-align: right;"
        }
        form.fields["gender"].widget.attrs = {
            "placeholder": "جنسیت",
            "style": "text-align: right;"
        }
        form.fields["bio"].widget.attrs = {
            "placeholder": "بیوگرافی",
            "style": "text-align: right;"
        }
        form.fields["language"].widget.attrs = {
            "placeholder": "زبان",
            "style": "text-align: right;"
        }
        form.fields["currency"].widget.attrs = {
            "placeholder": "واحد پول",
            "style": "text-align: right;"
        }
        form.fields["avatar"].widget.attrs = {
            "placeholder": "عکس",
            "style": "text-align: right;"
        }

        return form


class UpdatePasswordView(mixins.LoggedInOnlyView, SuccessMessageMixin,PasswordChangeView):
    template_name = "users/update_password.html "

    success_message = "رمز تغییر یافت"

    def get_form(self, form_class=None):
        form = super().get_form(form_class = form_class)
        form.fields["old_password"].widget.attrs = {"style": "text-align: right;","placeholder": "رمز فعلی"}
        form.fields["new_password1"].widget.attrs = {"style": "text-align: right;","placeholder": "رمز جدید"}
        form.fields["new_password2"].widget.attrs = {"style": "text-align: right;","placeholder": "تکرار رمز"}

        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()


@login_required
def switch_hosting(request):
    try:
        del request.session["is_hosting"]
    except KeyError:
        request.session["is_hosting"] = True
    return redirect(reverse("core:home"))


def switch_language(request):
    lang = request.GET.get("lang", None)
    if lang is not None:
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
    return HttpResponse(status=200)