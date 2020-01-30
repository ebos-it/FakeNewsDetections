from django import forms
from .models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    date_posted = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    fake_status = forms.BooleanField(required=False)

    class Meta:
        model = NewsArticle
        fields = ["title", "content", "author", "date_posted", "fake_status"]
