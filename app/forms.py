""" form of app """
from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile


class UserForm(forms.ModelForm):
    """ django user """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'password2')

    def clean_username(self):
        super(UserForm, self).clean()
        name = self.cleaned_data.get('username')
        if len(name) < 4:
            raise forms.ValidationError(
                "Name should be greater than 4 letters")
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already exists")
        return email

    def clean(self):
        # cleaned_data=super(EmployeeForm, self).clean()
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password and password2 and password == password2:
            print("pwd ok")
        return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    """ extend user model """
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 3}))
    contact = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    postal_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('address', 'contact', 'postal_code',)
