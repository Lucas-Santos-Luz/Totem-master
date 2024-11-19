from django import forms
from .models import Curso

# Formulário baseado no modelo Curso para criar ou editar cursos
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso  # Modelo associado ao formulário
        fields = [
            'nome', 'descricao', 'informacoes', 'requisitos', 'video', 'foto',
            'link_informacoes', 'link_interesses', 'gratuitos', 'pago',
            'presencial', 'aprendizagem_continuada', 'aprendizagem_industrial', 'tecnicos'
        ]  # Campos do modelo Curso que serão incluídos no formulário

        # Etiquetas para cada campo, que serão exibidas na interface
        labels = {
            'nome': 'Nome do Curso',
            'descricao': 'Descrição',
            'informacoes': 'Informações Adicionais',
            'requisitos': 'Requisitos',
            'video': 'Link do Vídeo (opcional)',
            'foto': 'Foto',
            'link_interesses': 'Link Interesses',
            'link_informacoes': 'Link Informações',
            'gratuitos': 'Gratuito',
            'pago': 'Pago',
            'presencial': 'Presencial',
            'aprendizagem_continuada': 'Aprendizagem Continuada',
            'aprendizagem_industrial': 'Aprendizagem Industrial',
            'tecnicos': 'Técnico'
        }

        # Widgets personalizados para cada campo, que ajustam a aparência e o comportamento dos inputs
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'informacoes': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'requisitos': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'video': forms.URLInput(attrs={'placeholder': 'https://example.com/video'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'link_informacoes': forms.URLInput(attrs={'placeholder': 'https://example.com/link'}),
            'link_interesses': forms.URLInput(attrs={'placeholder': 'https://example.com/link'}),
            'gratuitos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'presencial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'aprendizagem_continuada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'aprendizagem_industrial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tecnicos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
