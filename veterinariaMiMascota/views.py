from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import CitaForm
from .models import Cita, UserProfile


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    pet_name = forms.CharField(label='Nombre de la mascota', required=True)
    pet_breed = forms.CharField(label='Raza', required=True)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Teléfono', required=True)

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'pet_name', 'pet_breed', 'email', 'phone')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso. Por favor elige otro.')
        return username

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear un perfil de usuario para almacenar información adicional
            profile = UserProfile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                pet_name=form.cleaned_data['pet_name'],
                pet_breed=form.cleaned_data['pet_breed'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        # Agregar atributos a los campos del formulario
        form.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario', 'required': True})
        form.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña', 'required': True})
        form.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña', 'required': True})
        form.fields['first_name'].widget.attrs.update({'placeholder': 'Nombre', 'required': True})
        form.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido', 'required': True})
        form.fields['pet_name'].widget.attrs.update({'placeholder': 'Nombre de la mascota', 'required': True})
        form.fields['pet_breed'].widget.attrs.update({'placeholder': 'Raza', 'required': True})
        form.fields['email'].widget.attrs.update({'placeholder': 'E-mail', 'required': True})
        form.fields['phone'].widget.attrs.update({'placeholder': 'Télefono', 'required': True})
    return render(request, 'register.html', {'form': form})



@login_required
def user_data(request):
    data = {
        'username': request.user.username,
    }
    return JsonResponse(data)

def login_or_register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = get_user_model()
        # Verificar las credenciales del usuario e iniciar su sesión
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'reservar_cita')
            return redirect(next_url)
        else:
            # Mostrar un mensaje de error
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'login.html')
    else:
        # Mostrar el formulario de inicio de sesión
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def my_view(request):
    return render(request, 'index.html')

def servicios_page(request):
    return render(request, 'index.html')

def pet_shop_page(request):
    return render(request, 'index.html')

def blog_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'index.html')

def contacto_page(request):
    return render(request, 'index.html')




@login_required
def reservar_cita(request):
    print(request.user.is_authenticated)

    dias = {
        'Lunes': 1,
        'Martes': 2,
        'Miércoles': 3,
        'Jueves': 4,
        'Viernes': 5,
        'Sábado': 6,
    }
    
    # Obtener el día actual
    dia_actual = timezone.now().strftime('%A')
    
    # Verificar si el día actual es domingo y, en caso afirmativo, establecer el día actual como lunes
    if dia_actual == 'Sunday':
        dia_actual = 'Monday'
    
    # Crear un diccionario de traducción para convertir el nombre del día en inglés al nombre del día en español
    dias_en_es = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
    }
    
    # Convertir el nombre del día en inglés al nombre del día en español
    dia_actual_es = dias_en_es[dia_actual]
    
    # Crear una lista ordenada de los días a partir del día actual
    dias_ordenados = list(dias.keys())[list(dias.keys()).index(dia_actual_es):] + list(dias.keys())[:list(dias.keys()).index(dia_actual_es)]
    
    # Crear un nuevo diccionario de días que contenga solo los días a partir del día actual
    dias = {dia: dias[dia] for dia in dias_ordenados}
    
    return render(request, 'reservar_cita.html', {'dias': dias})


dias = {
        'Lunes': 1,
        'Martes': 2,
        'Miércoles': 3,
        'Jueves': 4,
        'Viernes': 5,
        'Sábado': 6,

    }
@login_required
def lista_de_horas(request, dia):
    # Obtener el usuario registrado
    user = request.user
    # Obtener el perfil de usuario asociado con el usuario registrado
    profile = UserProfile.objects.get(user=user)
    # Calcula las horas disponibles para el día seleccionado
    horas_disponibles = ['8:00','9:00', '10:00', '11:00', '12:00', '16:00', '17:00', '18:00', '19:00','20:00']
    # Recupera las citas creadas para el día seleccionado
    citas = Cita.objects.filter(dia=dia)
    # Crea una lista de tuplas con la hora y las citas para esa hora
    horas_con_citas = []
    for hora in horas_disponibles:
        citas_para_hora = [cita for cita in citas if cita.hora_texto == hora]
        horas_con_citas.append((hora, citas_para_hora))
    
    dias_invertidos = {valor: dia for dia, valor in dias.items()}
    nombre_dia = dias_invertidos[int(dia)]
    
    return render(request, 'lista_de_horas.html', {'dia': dia, 'horas_con_citas': horas_con_citas, 'nombre_dia': nombre_dia, 'profile': profile})



def crear_cita(request, dia, hora):
    # Obtener el usuario registrado
    user = request.user
    # Obtener el perfil de usuario asociado con el usuario registrado
    profile = UserProfile.objects.get(user=user)
    # Comprobar si el usuario ya tiene una cita para el día seleccionado
    if Cita.objects.filter(dia=dia, nombre_dueno=profile.first_name).exists():
        # Mostrar un mensaje de error
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False})
        else:
            messages.error(request, 'Ya tienes una cita para este día')
            return redirect('lista_de_horas', dia=dia)
    else:
        # Crear una nueva cita con los datos del perfil de usuario
        cita = Cita.objects.create(
            user=profile,
            dia=dia,
            hora=hora,
            hora_texto=hora,
            nombre_dueno=profile.first_name,
            nombre_mascota=profile.pet_name,
            raza=profile.pet_breed,
            email=profile.email,
            telefono=profile.phone
        )
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'nombre_mascota': profile.pet_name,
                'nombre_dueno': profile.first_name,
                'eliminar_cita_url': reverse('eliminar_cita', args=[dia, hora])
            })
        else:
            messages.success(request, 'Cita creada')
            return redirect('lista_de_horas', dia=dia)






def eliminar_citas():
    dias = {
        'Lunes': 1,
        'Martes': 2,
        'Miércoles': 3,
        'Jueves': 4,
        'Viernes': 5,
        'Sábado': 6,
    }
    
    # Obtener el último día en el diccionario dias
    ultimo_dia = list(dias.keys())[-1]
    
    # Eliminar las citas del último día
    Cita.objects.filter(dia=dias[ultimo_dia]).delete()
    
def eliminar_cita(request, dia, hora):
    # Obtener el usuario registrado
    user = request.user
    # Obtener el perfil de usuario asociado con el usuario registrado
    profile = UserProfile.objects.get(user=user)
    # Obtener la cita que coincide con el día, hora y usuario
    cita = Cita.objects.get(dia=dia, hora_texto=hora, nombre_dueno=profile.first_name)
    # Eliminar la cita
    cita.delete()
    messages.success(request, 'Cita eliminada')
    return redirect('lista_de_horas', dia=dia)

@login_required
def perfil_usuario(request):
    # Obtener el usuario registrado
    user = request.user
    # Obtener el perfil de usuario asociado con el usuario registrado
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        # Imprimir los valores de los campos del formulario
        print(f"first_name: {request.POST['first_name']}")
        print(f"last_name: {request.POST['last_name']}")
        print(f"pet_name: {request.POST['pet_name']}")
        print(f"pet_breed: {request.POST['pet_breed']}")
        print(f"email: {request.POST['email']}")
        print(f"phone: {request.POST['phone']}")
        # Actualizar el perfil de usuario con los datos del formulario
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.pet_name = request.POST['pet_name']
        profile.pet_breed = request.POST['pet_breed']
        profile.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.save()
        # Actualizar las citas existentes con los nuevos datos del perfil de usuario
        Cita.objects.filter(user=profile).update(

            nombre_dueno=profile.first_name,
            nombre_mascota=profile.pet_name,
            raza=profile.pet_breed,
            email=profile.email,
            telefono=profile.phone
        )
        messages.success(request, 'Perfil actualizado')
    return render(request, 'perfil_usuario.html', {'profile': profile})




