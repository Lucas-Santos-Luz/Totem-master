from django import forms

from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'informacoes', 'requisitos', 'video', 'foto', 'link_informacoes', 'link_interesses']
        labels = {
            'nome': 'Nome do Curso',
            'descricao': 'Descrição',
            'informacoes': 'Informações Adicionais',
            'requisitos': 'Requisitos',
            'video': 'Link do Vídeo (opcional)',
            'foto': 'foto',
            'link_interesses': 'Link_interesses',
            'link_informacoes': 'Link_informacoes',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'informacoes': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'requisitos': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'video': forms.URLInput(attrs={'placeholder': 'https://example.com/video'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'link interesse': forms.URLInput(attrs={'placeholder': 'https://example.com/link'}),
            'link informacoes': forms.URLInput(attrs={'placeholder': 'https://example.com/link'}),
        }
