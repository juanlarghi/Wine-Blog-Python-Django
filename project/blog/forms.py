from django import forms
from . import models

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = "__all__"
    