
from random import choices
from django import forms

from .models import Post,Category,Comment

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','thumbnail','title_tag','author','category','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'This is Title Placeholder '}),
            'title_tag': forms.TextInput(attrs= {'class': 'form-control'}),
            #'thumbnail': forms.ImageField(),
           # 'author': forms.Select(attrs= {'class': 'form-control'}),
            'author': forms.TextInput(attrs= {'class': 'form-control', 'value': '' , 'id': 'username' , 'type':'hidden'}),
            'category': forms.Select(choices = choice_list, attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            'snippet': forms.Textarea(attrs= {'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','thumbnail','title_tag','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'This is Title Placeholder '}),
            'title_tag': forms.TextInput(attrs= {'class': 'form-control'}),
           # 'author': forms.Select(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            'snippet': forms.Textarea(attrs= {'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'This is Title Placeholder '}),
           
           # 'author': forms.Select(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
        }