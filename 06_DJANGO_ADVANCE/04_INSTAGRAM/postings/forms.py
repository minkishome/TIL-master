from django import forms
from .models import Posting, Image

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content', )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', ) 
        widgets = {
            'file' : forms.FileInput(attrs={'multiple': True})
        }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         models = Comment
#         fields = ('content', )