from django import forms
from django.utils.translation import ugettext_lazy as _
from syncr_pinax.delicious.models import *

from tagging.forms import TagField

class DeliciousAccountForm(forms.ModelForm):
    """
    Delicious account
    """
    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^\w+$')
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, account=None, *args, **kwargs):
        self.account = account
        super(DeliciousAccountForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        return super(DeliciousAccountForm, self).save(commit)
        
    class Meta:
        model = DeliciousAccount
        fields = ("username",)


class TagForm(forms.ModelForm):
    tags = TagField(label="Tags", required=False)
    

class DeliciousSyncr(forms.ModelForm):
    tags = TagField(label="Tags", required=False)
