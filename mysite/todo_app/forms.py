from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    "maxLength": 100,
                                    "placeholder": "Title",
                                    "class": "form-control",
                                    "autofocus": True,
                                    }
                                )
                            )
    class Meta:
        model = Task
        fields = ('title',)
