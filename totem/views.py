from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages

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
    return render(request, 'totem/adm/loginADM.html')

def relatorioInteresses(request):
    return render(request, 'totem/adm/relatorioInteresses.html')

def relatorioFeedback(request):
    return render(request, 'totem/adm/relatorioFeedback.html')

def relatorioGeral(request):
    return render(request, 'totem/adm/relatorioGeral.html')

def sobreEscola(request):
    feedbacks = Feedback.objects.all()
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

def editarCursos(request):
    return render(request, 'totem/adm/editcurso.html')

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
            messages.success(request, 'Feedback enviado com sucesso!')
            return redirect('telaMenu')  # Redireciona para a página do menu após a submissão
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'totem/feedback.html')


from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm
from django.urls import reverse


def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        print("GET request, criando formulário vazio")  # Adicione isso para depurar
        form = CursoForm()

    return render(request, 'totem/adm/cadastroCurso.html', {'form': form})

def cursos(request):
    query = request.GET.get('search', '')
    cursos = Curso.objects.all()

    if query:
        cursos = cursos.filter(nome__icontains=query) | cursos.filter(descricao__icontains=query)

    return render(request, 'totem/cursos.html', {'cursos': cursos, 'query': query})
def detalhesCursos(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'totem/detalhesCursos.html', {'curso': curso})

def lista_feedbacks(request):
    feedbacks = Feedback.objects.all()  # Busca todos os feedbacks no banco
    return render(request, 'totem/sobreEscola.html', {'feedback': feedbacks})


def grafico_feedbacks(request):
    feedbacks = Feedback.objects.all()  # Obtém todos os feedbacks do banco de dados
    ratings = [feedback.rating for feedback in feedbacks]  # Extrai apenas os ratings
    return render(request, 'totem/adm/relatorioGeral.html', {'ratings': ratings})