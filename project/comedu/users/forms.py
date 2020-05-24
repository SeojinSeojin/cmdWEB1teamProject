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
