from django.urls import path
from totem.views import feedback_form,telaMenu, telaSuspensa, calendario, loginADM, relatorioInteresses, sobreEscola, feedback, detalhesCursos, formInteresse, relatorioFeedback, relatorioGeral, menuADM, menuREL, trilhaTI, trilhaAutomob, segInfra, editarCursos, cursos, trilhaNuvem, trilhaEletrica, trilhaInspetorQuali, adicionar_curso

urlpatterns = [
    path('', telaSuspensa, name='telaSuspensa'),
    path('telaMenu', telaMenu, name='telaMenu'),
    path('calendario', calendario, name='calendario'),
    path('loginADM', loginADM, name='loginADM'),
    path('relatorioInteresses', relatorioInteresses, name='relatorioInteresses'),
    path('sobreEscola', sobreEscola, name='sobreEscola'),
    path('feedback', feedback, name='feedback'),
    path('formInteresse', formInteresse, name='formInteresse'),
    path('curso/<int:curso_id>/', detalhesCursos, name='detalhesCursos'),
    path('relatorioFeedback', relatorioFeedback, name='relatorioFeedback'),
    path('relatorioGeral', relatorioGeral, name='relatorioGeral'),
    path('menuADM', menuADM, name='menuADM'),
    path('menuREL', menuREL, name='menuREL'),
    path('adicionar/', adicionar_curso, name='cadastroCurso'),
    path('trilhaTI/', trilhaTI, name='trilhaTI'),
    path('trilhaAutomob', trilhaAutomob, name='trilhaAutomob'),
    path('segInfra/', segInfra, name='segInfra'),
    path('editarCursos', editarCursos, name='editarCursos'),
    path('cursos', cursos, name='cursos'),
    path('trilhaNuvem/', trilhaNuvem, name='trilhaNuvem'),
    path('trilhaEletrica', trilhaEletrica, name='trilhaEletrica'),
    path('trilhaInspetorQuali', trilhaInspetorQuali, name='trilhaInspetorQuali'),
    path('feedback/', feedback_form, name='feedback'),

]



