"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""

from django import forms
from app_data_off.management.commands.constante import list_categories


class SearchForm(forms.Form):
    """ Form to search a substitut. Display on nav and index page. """
    search = forms.CharField(max_length=150)


# class DropDownCategory(forms.Form):
#     """ Form to display categories on the search dropdown list to search substituts. """
#     dropdown = forms.ChoiceField(choices=list_categories)
