from django import forms


class TodoForm(forms.Form):
    description = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Description of your to do',
            'id': 'newtodo',
        })
    )
