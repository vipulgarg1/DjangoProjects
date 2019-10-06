from django import forms

class Videoform(forms.Form):
    videoname = forms.CharField(max_length=30,
        widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Name',
        'id':'inputname',
        }))

    videodesc = forms.CharField(max_length=100,
        widget = forms.Textarea(attrs={
        'class':'form-control',
        'rows':'5',
        'id':'comment',
        'placeholder':'Comment',
        }))
