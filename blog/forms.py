from django import forms
from blog.models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields= ['name','email','image','message']

 