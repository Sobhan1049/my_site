from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"style": "text-align: right;",'placeholder': 'ایمیل'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"style": "text-align: right;",'placeholder': 'رمز'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error('password', forms.ValidationError('password incorrect'))
        except:
            self.add_error('email', forms.ValidationError('user does not exist'))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields =('first_name','last_name', 'email',)
        widgets = {
            'first_name': forms.TextInput(attrs={"style": "text-align: right;",'placeholder': 'نام'}),
            'last_name':forms.TextInput(attrs={"style": "text-align: right;",'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={"style": "text-align: right;",'placeholder': 'ایمیل'})
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={"style": "text-align: right;",'placeholder': 'رمز'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"style": "text-align: right;", 'placeholder': 'تکرار رمز'}))

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("password does not match")
        else:
            return password

    def save(self, *args,**kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()