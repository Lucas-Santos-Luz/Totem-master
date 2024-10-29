# formulario_app/models.py

from django.db import models

class Feedback(models.Model):
    nome = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.feedback[:50]}"


from django.db import models

class Curso(models.Model):
    link_informacoes = models.URLField(blank=True, null=True)
    link_interesses = models.URLField(blank=True, null=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    informacoes = models.TextField()
    requisitos = models.TextField()
    video = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.nome