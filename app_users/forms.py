"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""
from django import forms
# the only drawback of UserCreationForm is that it doesn't have email field. As a result, we can't use it to send
# email verification to the user to verify the account.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    # Customize the Django UserCreationForm because has only 3 fields  username (from USER model), password1 and
    # password2

    email = forms.EmailField(required = True)  # the email field is declared

    # class meta allows to precise with which data class NewUserForm can work
    class Meta:
        model = User  # attribute model, specify here the model that we want to link to the form
        fields = ("username", "email", "password1", "password2")  # fields that we want to display

    # function that overwrites the default save function to include the email field we added
    def save(self, commit = True):
        #  commit=False, then it will return an object that hasn't yet been saved to the database.
        # important to call the method of the parent class with super().save(*args, **kwargs)) to record in db
        user = super(NewUserForm, self).save(commit = False)
        user.email = self.cleaned_data['email']  # the dictionary clean_data contains valid fields
        if commit:
            user.save()
        return user
