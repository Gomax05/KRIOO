from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from finanzas.views import (
    dashboard,
    registrar_finanza,
    editar_finanza,
    eliminar_finanza,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # corregido

    # Vistas principales
    path('', dashboard, name='dashboard'),
    path('registrar/', registrar_finanza, name='registrar_finanza'),
    path('editar/<int:pk>/', editar_finanza, name='editar_finanza'),
    path('eliminar/<int:pk>/', eliminar_finanza, name='eliminar_finanza'),

    # API
    path('api/', include('finanzas.api_urls')),
]

from finanzas.views import registro_usuario

urlpatterns += [
    path('registrarse/', registro_usuario, name='registrarse'),
]
