from django import forms
from .models import Comment
#Here we inhert from the base class forms 
class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  # This has email verification built in
  email = forms.EmailField()
  to = forms.EmailField()
  comments = forms.CharField(required=False,
                            widget=forms.Textarea)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')