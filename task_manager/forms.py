from django import forms
from .models import Task, Comment, Dashboard

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'archived']

    def __init__(self, *args,  **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['created_by'].initial = user

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        #self.fields['created_by'].widget.attrs['class'] = 'form-control'
        #self.fields['assigned_to'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        #self.fields['archived'].widget.attrs['class'] = 'form-control'


