from nomina import calcular_sueldo
def reporte(empleados_d):
    for empleado in empleados_d:
        sueldo_f=calcular_sueldo(empleado['horas_trabajadas'],empleado['valor_hora'])
        print(f"El empleado: {empleado['Nombre']} gana: {sueldo_f}")