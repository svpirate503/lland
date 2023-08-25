from django import forms


    

class contact_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea'}))
    

