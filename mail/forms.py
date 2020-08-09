from django import forms


class ContactForm(forms.Form):
    text = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    timer = forms.DecimalField(label='Время', widget=forms.NumberInput(attrs={'class': 'form-control'}))
