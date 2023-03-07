from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task

class CreateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'important',
        )
        labels = {
            'name': _('Título'),
            'description': _('Descripción'),
            'important': _('Importante'),
        }
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'id':'name',
                    'class':'',
                    'type':'text',
                    'minlength':1,
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'id':'description',
                    'class':'',
                    'type':'textarea',
                    'minlength':1,
                }
            ),
        }