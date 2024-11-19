from .models import Feedback
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Curso, InteresseCurso, Login
from .forms import CursoForm
from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse
from django.db import IntegrityError
import os
from django.conf import settings


def telaMenu(request):
    return render(request, 'totem/menus/telaMenu.html')

def menuADM(request):
    return render(request, 'totem/menus/menuADM.html')

def menuREL(request):
    return render(request, 'totem/menus/menuREL.html')
def telaSuspensa(request):
    return render(request, 'totem/telaSuspensa.html')

def calendario(request):
    return render(request, 'totem/calendario.html')

def loginADM(request):
    # Usuário e senha pré-definidos
    usuario_pre = "admin@801"
    senha_pre = "123"

    # Verifique se o usuário já existe no banco
    if not Login.objects.filter(usuario=usuario_pre).exists():

       Login.objects.create(
           usuario=usuario_pre,
           senha=senha_pre
       )

    # Renderiza a página de login
    if request.method == "POST":
        # Lógica de autenticação
        return redirect('menuADM')  # Substitua 'home' pela página após o login bem-sucedido
    return render(request, 'totem/adm/loginADM.html')


def relatorioFeedback(request):
    feedbacks = Feedback.objects.all()

    # Dados para o gráfico
    labels = ['Excelente', 'Bom', 'Regular', 'Ruim', 'Péssimo']
    data = [
        feedbacks.filter(rating=5).count(),
        feedbacks.filter(rating=4).count(),
        feedbacks.filter(rating=3).count(),
        feedbacks.filter(rating=2).count(),
        feedbacks.filter(rating=1).count(),
    ]

    return render(request, 'totem/adm/relatorioFeedback.html', {
        'feedbacks': feedbacks,
        'labels': json.dumps(labels),
        'data': json.dumps(data)
    })


def relatorioGeral(request):
    return render(request, 'totem/adm/relatorioGeral.html')

def sobreEscola(request):
    feedbacks = Feedback.objects.all().order_by('-rating')
    return render(request, 'totem/sobreEscola.html', {'feedbacks': feedbacks})


def feedback(request):
    return render(request, 'totem/feedback.html')

def formInteresse(request):
    return render(request, 'totem/formInteresse.html')

def trilhaTI(request):
    return render(request, 'totem/trilhas/trilhasTI/trilhaTI.html')

def trilhaAutomob(request):
    return render(request, 'totem/trilhas/trilhaAutomob.html')

def segInfra(request):
    return render(request, 'totem/trilhas/trilhasTI/segInfra.html')



def trilhaNuvem(request):
    return render(request, 'totem/trilhas/trilhasTI/trilhaNuvem.html')

def trilhaEletrica(request):
    return render(request, 'totem/trilhas/trilhaEletrica.html')

def trilhaInspetorQuali(request):
    return render(request, 'totem/trilhas/trilhaInspetorQuali.html')


def feedback_form(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        feedback = request.POST.get('feedback')
        rating = request.POST.get('fb')

        if nome and feedback:
            Feedback.objects.create(nome=nome, feedback=feedback, rating=int(rating))
            return redirect('agradecimento')  # Redireciona para a página do menu após a submissão
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'totem/feedback.html')


def agradecimento(request):
    return render(request, 'totem/menus/agradecimento.html')


def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('telaeditCursos')
    else:
        print("GET request, criando formulário vazio")  # Adicione isso para depurar
        form = CursoForm()

    return render(request, 'totem/adm/cadastroCurso.html', {'form': form})

def cursos(request):
    query = request.GET.get('search', '')
    tags = request.GET.getlist('tags')

    cursos = Curso.objects.all()

    # Aplicando o filtro de busca
    if query:
        cursos = cursos.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))

    # Filtro por tags
    if tags:
        tag_filters = Q()
        if 'gratuitos' in tags:
            tag_filters |= Q(gratuitos=True)
        if 'pago' in tags:
            tag_filters |= Q(pago=True)
        if 'presencial' in tags:
            tag_filters |= Q(presencial=True)
        if 'aprendizagem_continuada' in tags:
            tag_filters |= Q(aprendizagem_continuada=True)
        if 'aprendizagem_industrial' in tags:
            tag_filters |= Q(aprendizagem_industrial=True)
        if 'tecnicos' in tags:
            tag_filters |= Q(tecnicos=True)
        cursos = cursos.filter(tag_filters)

    context = {
        'cursos': cursos,
        'query': query,
    }
    return render(request, 'totem/cursos.html', context)


def editarCursos(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('telaeditCursos')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'totem/adm/editarCurso.html', {'form': form, 'id': id})


def deletarCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('telaeditCursos')

def telaeditCursos(request):
    query = request.GET.get('search', '')
    cursos = Curso.objects.all()

    if query:
        cursos = cursos.filter(nome__icontains=query) | cursos.filter(descricao__icontains=query)

    return render(request, 'totem/adm/telaeditCursos.html', {'cursos': cursos, 'query': query})

def registrar_interesse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    interesse, created = InteresseCurso.objects.get_or_create(curso=curso)

    # Incrementar o número de cliques
    interesse.num_cliques += 1
    interesse.save()

    return JsonResponse({'status': 'sucesso', 'num_cliques': interesse.num_cliques})

def detalhesCursos(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    # Obter o número de cliques para este curso
    interesse = InteresseCurso.objects.filter(curso=curso).first()
    num_cliques = interesse.num_cliques if interesse else 0

    return render(request, 'totem/detalhesCursos.html', {
        'curso': curso,
        'num_cliques': num_cliques
    })

def relatorioInteresses(request):
    cursos = Curso.objects.annotate(num_cliques_total=Sum('interessecurso__num_cliques'))

    # Dados para o gráfico
    labels = [curso.nome for curso in cursos]
    data = [curso.num_cliques_total or 0 for curso in cursos]

    return render(request, 'totem/adm/relatorioInteresses.html', {
        'cursos': cursos,
        'labels': labels,
        'data': data
    })

def validar_login(request):
    if request.method == 'POST':
        # Extraímos o nome de usuário e senha dos dados da forma
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # Verificamos se o nome de usuário existe no banco de dados
        user = Login.objects.filter(usuario=usuario).first()

        if user and user.senha == int(senha):
            # Redireciona para o painel ou página inicial
            return redirect('menuADM')
        else:
            # Credenciais incorretas
            messages.error(request, "Usuário de usuário ou senha inválido")

        # Renderiza o template de login
    return render(request, 'totem/adm/loginADM.html')


