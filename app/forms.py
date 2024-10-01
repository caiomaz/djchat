from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control message-input',
                'style': 'resize: none; height: 100px;',  # Altura fixa e impedir redimensionamento
            }),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) > 100:
            raise forms.ValidationError('O texto não pode exceder 100 caracteres.')
        return text
