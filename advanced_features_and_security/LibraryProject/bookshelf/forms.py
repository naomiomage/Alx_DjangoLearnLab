# bookshelf/forms.py
from django import forms
from .models import Book

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

        # Optional: add nice widgets for better UX
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Book Title"}),
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Author Name"}),
            "published_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
