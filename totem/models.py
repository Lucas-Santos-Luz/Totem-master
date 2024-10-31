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

    gratuitos = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)
    presencial = models.BooleanField(default=False)
    aprendizagem_continuada = models.BooleanField(default=False)
    aprendizagem_industrial = models.BooleanField(default=False)
    tecnicos = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class InteresseCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)  # Data e hora do clique
    num_cliques = models.IntegerField(default=0)

    def __str__(self):
        return f"Interesse no curso {self.curso.nome} - {self.num_cliques} cliques"

class Login(models.Model):
    usuario = models.CharField(max_length=255)
    senha = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.usuario