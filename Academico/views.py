from django.shortcuts import render
from .models import Curso

# Create your views here.


def home(request):
    cursoListados = Curso.objects.all()
    return render(request, "gestaoCursos.html", {"cursos": cursoListados})
