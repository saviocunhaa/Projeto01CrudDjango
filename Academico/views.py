from django.shortcuts import redirect, render

from .models import Curso

# Create your views here.


def home(request):
    cursoListados = Curso.objects.all()
    return render(request, "gestaoCursos.html", {"cursos": cursoListados})


def registrarCursos(request):
    codigo = request.POST['txtCodigo']
    nome = request.POST['txtNome']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.create(codigo=codigo, nome=nome, creditos=creditos)
    return redirect('/')
