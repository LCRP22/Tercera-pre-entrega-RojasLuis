from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, ProfesoresFormulario, EstudiantesFormulario, EntregablesFormulario


# Create your views here.

def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):

      return render(request, "AppCoder/cursos.html")

def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):

      if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()

      return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def profesoresFormulario(request):

      if request.method == "POST":

            miFormulario = ProfesoresFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
                  profesor.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = ProfesoresFormulario()

      return render(request, "AppCoder/profesoresFormulario.html", {"miFormulario": miFormulario})

def estudiantesFormulario(request):

      if request.method == "POST":

            miFormulario = EstudiantesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EstudiantesFormulario()

      return render(request, "AppCoder/estudiantesFormulario.html", {"miFormulario": miFormulario})

def entregablesFormulario(request):

      if request.method == "POST":

            miFormulario = EntregablesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  entregable = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fecha"], entregado=informacion["entregado"])
                  entregable.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EntregablesFormulario()

      return render(request, "AppCoder/entregablesFormulario.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
      return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):

      respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)


