from django import forms
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)


from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')

from blog.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','author','body','status',)
