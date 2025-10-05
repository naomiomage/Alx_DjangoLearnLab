# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget  # ✅ Import TagWidget
from .models import Post, Comment


# --- USER FORMS ---

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")


# --- POST FORM ---

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags here
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post...'}),
            'tags': TagWidget(),  # ✅ Taggit widget for tags input
        }


# --- COMMENT FORM ---

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write your comment...'}
            )
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError('Comment cannot be empty.')
        return content
