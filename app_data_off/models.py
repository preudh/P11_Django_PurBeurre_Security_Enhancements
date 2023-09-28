# Create your models here.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# no verbose name added on attributes to simplify


""" Models declaration """

from django.db import models
from django.contrib.auth.models import User


# Using the Django authentication system
# User objects represent the people who interact with your site and are used to activate features such as restricting
# access, registering user profiles, associating content with its creator, etc.


class Category(models.Model):
    """ category model for product"""

    name = models.CharField(max_length=150)

    def __str__(self):  # for debug
        return self.name


class Product(models.Model):
    """ Product model"""

    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    store = models.CharField(max_length=150)
    nutrition_grade = models.CharField(max_length=1)
    url = models.URLField(max_length=150)
    image_front_url = models.URLField(max_length=150)
    image_nutrition_small_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)  # delete all the category model

    def __str__(self):
        return self.name


class UserProduct(models.Model):
    """ Favourite product model. Reference table between Product and User. """

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
