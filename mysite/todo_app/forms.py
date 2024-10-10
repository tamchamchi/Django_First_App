from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Title",
                                    "class": "form-control",
                                    "autofocus": True,
                                    }
                                )
                            )
    class Meta:
        model = Task
        fields = ('title',)
