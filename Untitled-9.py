# Carreras y tipos de acceso a internet
carreras = ['Ingeniería', 'Derecho', 'Medicina']
tipos_acceso = ['estable', 'intermitente', 'no tiene']

# Crear estructura de datos para guardar los resultados
resultados = {
    carrera: {'estable': 0, 'intermitente': 0, 'no tiene': 0}
    for carrera in carreras
}

# Recorrer cada carrera
for carrera in carreras:
    print(f"\nCarrera: {carrera}")
    for grupo in range(1, 4):  # 3 grupos
        print(f"  Grupo {grupo}")
        for estudiante in range(1, 6):  # 5 estudiantes por grupo
            while True:
                acceso = input(f"    Estudiante {estudiante}, tipo de internet (estable, intermitente, no tiene): ").strip().lower()
                if acceso in tipos_acceso:
                    resultados[carrera][acceso] += 1
                    break
                else:
                    print("    Entrada inválida. Intenta de nuevo.")

# Mostrar resultados por carrera
print("\n--- Resultados por carrera ---")
totales = {'estable': 0, 'intermitente': 0, 'no tiene': 0}

for carrera, datos in resultados.items():
    print(f"\nCarrera: {carrera}")
    for tipo in tipos_acceso:
        cantidad = datos[tipo]
        print(f"  {tipo.capitalize()}: {cantidad}")
        totales[tipo] += cantidad

# Mostrar totales generales
print("\n--- Totales generales ---")
for tipo in tipos_acceso:
    print(f"{tipo.capitalize()}: {totales[tipo]}")
