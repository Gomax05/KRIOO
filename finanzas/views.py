from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroFinanciero
from .forms import RegistroForm
from .ia import sugerencia_financiera
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroFinanciero
from .forms import RegistroForm
from .ia import sugerencia_financiera
from .utils import generar_grafico_por_tipo
from django.db.models import Sum


# @login_required
# def dashboard(request):
#     registros = RegistroFinanciero.objects.filter(usuario=request.user).order_by('-fecha')
#     sugerencias = [sugerencia_financiera(r.tipo, r.monto) for r in registros]
#     datos = zip(registros, sugerencias)  # para mostrar ambos en el template
#     return render(request, 'dashboard.html', {
#         'registros': registros,
#         'sugerencias': sugerencias,
#         'datos': datos
#     })
from .utils import generar_grafico_por_tipo

# @login_required
# def dashboard(request):
#     registros = RegistroFinanciero.objects.filter(usuario=request.user).order_by('-fecha')
#     sugerencias = [sugerencia_financiera(r.tipo, r.monto) for r in registros]
#     datos = zip(registros, sugerencias)
#     grafico = generar_grafico_por_tipo(request.user)
#     return render(request, 'dashboard.html', {
#         'registros': registros,
#         'sugerencias': sugerencias,
#         'datos': datos,
#         'grafico': grafico
#     })

@login_required
def dashboard(request):
    registros = RegistroFinanciero.objects.filter(usuario=request.user).order_by('-fecha')
    sugerencias = [sugerencia_financiera(r.tipo, r.monto) for r in registros]
    datos = zip(registros, sugerencias)
    grafico = generar_grafico_por_tipo(request.user)

    ingresos = registros.filter(tipo='Ingreso').aggregate(total=Sum('monto'))['total'] or 0
    gastos = registros.filter(tipo='Gasto').aggregate(total=Sum('monto'))['total'] or 0
    ahorros = registros.filter(tipo='Ahorro').aggregate(total=Sum('monto'))['total'] or 0
    porcentaje_ahorro = round((ahorros / ingresos) * 100, 2) if ingresos > 0 else 0

    return render(request, 'dashboard.html', {
        'datos': datos,
        'grafico': grafico,
        'ingresos': ingresos,
        'gastos': gastos,
        'ahorros': ahorros,
        'porcentaje_ahorro': porcentaje_ahorro,
    })

@login_required
def registrar_finanza(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def registrar_finanza(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def editar_finanza(request, pk):
    registro = get_object_or_404(RegistroFinanciero, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro actualizado correctamente.")
            return redirect('dashboard')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'registro.html', {'form': form, 'editar': True})

@login_required
def eliminar_finanza(request, pk):
    registro = get_object_or_404(RegistroFinanciero, pk=pk, usuario=request.user)
    if request.method == 'POST':
        registro.delete()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect('dashboard')
    return render(request, 'confirmar_eliminacion.html', {'registro': registro})

from .forms import RegistroUsuarioForm
from django.contrib.auth import login

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})
