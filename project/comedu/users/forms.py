from django import forms
from . import models


class LoginForm(forms.Form):

    studentID = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        studentID = self.cleaned_data.get("studentID")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(studentID=studentID)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong"))
        except models.User.DoesnotExist:
            raise forms.ValidationError("User does not exist")


class SignUpForm(forms.Form):
    studentID = forms.CharField(max_length=10)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists!")
        except models.User.DoesNotExist:
            return email

    def clean_studentID(self):
        studentID = self.cleaned_data.get("studentID")
        try:
            models.User.objects.get(studentID=studentID)
            raise forms.ValidationError("User already exists!")
        except models.User.DoesNotExist:
            return studentID

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        studentID = self.cleaned_data.get("studentID")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(
            username, email=email, password=password, studentID=studentID)
        user.save()
