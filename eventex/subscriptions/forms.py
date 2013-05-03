# coding: utf-8

from django import forms
from eventex.subscriptions.models import Subscription

__author__ = 'mmj2286'

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription