from django import forms
from .models import ticket, comment, customer

class TicketForm(forms.ModelForm):
    class Meta:
        model  = ticket
        fields = '__all__'
        
    def __init__(self, *args,  **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['customer_name'].widget.attrs['class'] = 'form-control'
        self.fields['created_by'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = '__all__'

    def __init__(self, *args,  **kwargs):
        ticket =kwargs.pop('ticket',None)
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

        if ticket:
            self.fields['ticket'].initial = ticket
        if user:
            self.fields['user'].initial = user

        self.fields['ticket'].widget.attrs['class'] = 'form-control'
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
       
class CustomerForm(forms.ModelForm):
    class Meta:
        model  = customer
        fields = '__all__' 

    def __init__(self, *args,  **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
