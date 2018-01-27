from django import forms

from .models import*

class TopicForm(forms.ModelForm):
    """Formulário para adicionar um novo tópico"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
