from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppEntrega.models import Series, Peliculas, Premios


# Create your views here.


def inicio(request):

      return render(request, "AppEntrega/inicio.html")

def serie(request):

      return render(request, "AppEntrega/series.html")

def premios(request):

      return render(request, "AppEntrega/premios.html")

def peliculas(request):

      return render(request, "AppEntrega/peliculas.html")

def documentales(request):

    return render (request, "AppEntrega/documentales.html")

from AppEntrega.forms import PeliculaFormulario, PremiosFormulario, SeriesFormulario, UserRegisterForm


def premios(request):

      if request.method == "POST":
      
            miFormulario = PremiosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  premio = Premios(prelicula=informacion["premio"], premio=informacion["camada"], año=informacion["año"])
                  premio.save()
                  return render(request, "AppEntrega/inicio.html")
      
      else:
            miFormulario = PremiosFormulario()
            
      return render(request, "AppEntrega/Premios.html", {"miFormulario": miFormulario})


def peliculas(request):

      if request.method == "POST":
      
            miFormulario = PeliculaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  pelicula = Peliculas(nombre=informacion["nombre"], duracion=informacion["duracion"], critica=informacion["critica"])
                  pelicula.save()
                  return render(request, "AppEntrega/inicio.html")
      
      else:
            miFormulario = PeliculaFormulario()
            
      return render(request, "AppEntrega/Peliculas.html", {"miFormulario": miFormulario})





def series(request):

      if request.method == "POST":
      
            miFormulario = SeriesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  serie = Series(nombre=informacion["nombre"], cantidad_de_temporadas=informacion["temporadas"], valoracion=informacion["valoracion"])
                  serie.save()
                  return render(request, "AppEntrega/inicio.html")
      
      else:
            miFormulario = SeriesFormulario()
            
      return render(request, "AppEntrega/Series.html", {"miFormulario": miFormulario})



from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppEntrega/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppEntrega/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppEntrega/login.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppEntrega/login.html", {"form": form})


def register(request):

      if request.method == 'POST':

           # form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppEntrega/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
          #  form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppEntrega/registro.html" ,  {"form":form})


@login_required
def inicio(request):

    return render(request, "AppEntrega/inicio.html")



class PeliculasList(ListView):

    model = Peliculas
    template_name = "AppEntrega/peliculas_list.html"

class PeliculasDetalle(DetailView):

    model = Peliculas
    template_name = "AppEntrega/peliculas_detalle.html"

class PeliculasCreacion(CreateView):

    model = Peliculas
    success_url = "/AppEntrega/peliculas/list"
    fields = ['nombre', 'duracion', 'critica']

class PeliculasUpdate(UpdateView):

    model = Peliculas
    success_url = "/AppEntrega/peliculas/list"
    fields = ['nombre', 'duracion', 'critica']

class PeliculasDelete(DeleteView):

    model = Peliculas
    success_url = "/AppEntrega/peliculas/list"



class PremiosList(ListView):

    model = Premios
    template_name = "AppEntrega/premios_list.html"

class PremiosDetalle(DetailView):

    model = Premios
    template_name = "AppEntrega/premios_detalle.html"

class PremiosCreacion(CreateView):

    model = Premios
    success_url = "/AppEntrega/premios/list"
    fields = ['pelicula', 'premio', 'año']

class PremiosUpdate(UpdateView):

    model = Premios
    success_url = "/AppEntrega/premios/list"
    fields = ['pelicula', 'premio', 'año']

class PremiosDelete(DeleteView):

    model = Premios
    success_url = "/AppEntrega/premios/list"



class SeriesList(ListView):

    model = Series
    template_name = "AppEntrega/series_list.html"

class SeriesDetalle(DetailView):

    model = Series
    template_name = "AppEntrega/series_detalle.html"

class SeriesCreacion(CreateView):

    model = Series
    success_url = "/AppEntrega/series/list"
    fields = ['nombre', 'cantidad de temporadas', 'valoracion']

class SeriesUpdate(UpdateView):

    model = Series
    success_url = "/AppEntrega/series/list"
    fields = ['nombre', 'cantidad de temporadas', 'valoracion']

class SeriesDelete(DeleteView):

    model = Series
    success_url = "/AppEntrega/series/list"
