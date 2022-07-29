from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Name'}),label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),label="")
    message = forms.CharField(max_length=500, min_length=200,label="",widget=forms.Textarea(attrs={'placeholder': 'Message'}))