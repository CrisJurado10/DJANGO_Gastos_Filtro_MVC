from django.shortcuts import render
from .models import Gasto

def filtrar_gastos(request):
    gastos = []
    total_por_departamento = {}

    if request.method == "POST":
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        gastos = Gasto.objects.filter(fecha__range=[fecha_inicio, fecha_fin])

        for gasto in gastos:
            depto = gasto.empleado.departamento.nombre
            total_por_departamento[depto] = total_por_departamento.get(depto, 0) + gasto.monto

    return render(request, 'core/gastos.html', {
        'gastos': gastos,
        'totales': total_por_departamento,
    })
