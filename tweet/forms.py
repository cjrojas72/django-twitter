from django import forms
from tweet.models import Tweet


class AddTweetForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea, required=True)
