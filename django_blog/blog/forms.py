# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


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
    # Add a field for tags
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g., travel, life, coding)",
        widget=forms.TextInput(attrs={'placeholder': 'Add tags...'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags here
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post...'}),
        }

    def save(self, commit=True):
        """Override save method to handle tags manually."""
        post = super().save(commit=False)
        if commit:
            post.save()

        # Handle tags input (split by commas)
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]

        # Clear existing tags and reassign
        post.tags.clear()
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)

        return post


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
