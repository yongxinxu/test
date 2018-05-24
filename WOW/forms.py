from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from WOW.models import UserInfo


class UserForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'email']
        model = UserInfo

