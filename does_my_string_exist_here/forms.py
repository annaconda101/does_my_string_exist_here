from django import forms


class FindTextForm(forms.Form):
    text_to_search = forms.CharField(widget=forms.Textarea)
    subtext = forms.CharField(max_length=300)