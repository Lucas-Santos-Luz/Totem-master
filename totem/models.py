# formulario_app/models.py

from django.db import models

# Modelo para armazenar feedbacks dos usuários
class Feedback(models.Model):
    nome = models.CharField(max_length=100)  # Nome do usuário que deu o feedback
    feedback = models.TextField()  # Texto do feedback do usuário
    rating = models.IntegerField(null=True, blank=True)  # Classificação opcional (ex.: estrelas)

    def __str__(self):
        # Retorna o nome do usuário e os primeiros 50 caracteres do feedback
        return f"{self.nome} - {self.feedback[:50]}"

# Modelo para armazenar informações sobre cursos
class Curso(models.Model):
    link_informacoes = models.URLField(blank=True, null=True)  # Link opcional com informações sobre o curso
    link_interesses = models.URLField(blank=True, null=True)  # Link opcional para interesses adicionais
    nome = models.CharField(max_length=255)  # Nome do curso
    descricao = models.TextField()  # Breve descrição do curso
    informacoes = models.TextField()  # Informações detalhadas sobre o curso
    requisitos = models.TextField()  # Requisitos para participar do curso
    video = models.URLField(blank=True, null=True)  # Link opcional para um vídeo sobre o curso
    foto = models.ImageField(upload_to='images/', blank=True, null=True)  # Imagem opcional do curso

    # Tags booleanas para classificar o curso
    gratuitos = models.BooleanField(default=False)  # Indica se o curso é gratuito
    pago = models.BooleanField(default=False)  # Indica se o curso é pago
    presencial = models.BooleanField(default=False)  # Indica se o curso é presencial
    aprendizagem_continuada = models.BooleanField(default=False)  # Tag para cursos de aprendizagem continuada
    aprendizagem_industrial = models.BooleanField(default=False)  # Tag para cursos industriais
    tecnicos = models.BooleanField(default=False)  # Tag para cursos técnicos

    def __str__(self):
        # Retorna o nome do curso
        return self.nome

# Modelo para registrar o interesse em um curso
class InteresseCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  # Referência ao curso relacionado
    data = models.DateTimeField(auto_now_add=True)  # Data e hora do clique para registro de interesse
    num_cliques = models.IntegerField(default=0)  # Contador de cliques/interesses no curso

    def __str__(self):
        # Retorna o nome do curso e o número de cliques de interesse
        return f"Interesse no curso {self.curso.nome} - {self.num_cliques} cliques"

# Modelo para armazenar dados de login
class Login(models.Model):
    usuario = models.CharField(max_length=255)  # Nome de usuário
    senha = models.IntegerField(null=True, blank=True)  # Senha opcional (como número)

    def __str__(self):
        # Retorna o nome do usuário
        return self.usuario
