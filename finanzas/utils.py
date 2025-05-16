# finanzas/utils.py
import matplotlib.pyplot as plt
import io
import base64
from .models import RegistroFinanciero
from collections import defaultdict

def generar_grafico_por_tipo(usuario):
    registros = RegistroFinanciero.objects.filter(usuario=usuario).order_by('fecha')

    data = defaultdict(list)
    fechas = []

    for reg in registros:
        fechas.append(reg.fecha)
        data[reg.tipo].append(reg.monto)

    # Crear el gráfico
    plt.figure(figsize=(8, 4))
    for tipo, montos in data.items():
        plt.plot(fechas[:len(montos)], montos, label=tipo)

    plt.title("Evolución financiera")
    plt.xlabel("Fecha")
    plt.ylabel("Monto (S/.)")
    plt.legend()
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return imagen_base64
