def sugerencia_financiera(tipo, monto):
    if tipo == 'Ahorro' and monto < 200:
        return "Recomendación: Aumenta tu ahorro, idealmente el 20% de tus ingresos."
    elif tipo == 'Gasto' and monto > 1000:
        return "Alerta: Gasto elevado, evalúa si fue realmente necesario."
    return "¡Bien hecho! Tu registro es saludable."
