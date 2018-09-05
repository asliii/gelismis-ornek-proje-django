from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('auth','title', 'text')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'text-input-class'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editable-textarea postcontent'})
        }

class CommitForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('auth','text')

        widgets = {
            'auth': forms.TextInput(attrs={'class':'text-input-class'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editable-textarea'})
        }