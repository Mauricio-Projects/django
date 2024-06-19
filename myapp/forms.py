from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="title new task")
    description = forms.CharField(label="description task", widget=forms.Textarea)