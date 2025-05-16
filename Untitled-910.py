## Categorías y subcategorías de libros
categorias = {
    "Ingeniería": ["Sistemas", "civil", "Industrial"],
    "Salud": ["Enfermería", "Medicina", "Nutrición"],
    "Derecho": ["Penal", "tributario", "Constitucional"],
    "Literatura": ["Clásica", "Moderna", "Infantil"]
}

# Días de la semana
dias = 5

# Estructura de datos para guardar préstamos
prestamos = {
    categoria: {
        sub: [0] * dias for sub in subcategorias
    } for categoria, subcategorias in categorias.items()
}

# Registro de préstamos
for categoria, subcategorias in categorias.items():
    print(f"\nCategoría: {categoria}")
    for sub in subcategorias:
        print(f"  Subcategoría: {sub}")
        for dia in range(dias):
            while True:
                try:
                    cantidad = int(input(f"    Día {dia + 1}, préstamos: "))
                    if cantidad < 0:
                        print("    No se permiten números negativos.")
                        continue
                    prestamos[categoria][sub][dia] = cantidad
                    break
                except ValueError:
                    print("    Ingrese un número que sea válido.")

# resultados
total_general = 0
print("\n--- Reporte de préstamos ---")
for categoria, subcategorias in prestamos.items():
    print(f"\nCategoría: {categoria}")
    total_categoria = 0
    for sub, dias_lista in subcategorias.items():
        total_sub = sum(dias_lista)
        print(f"  Subcategoría {sub}: {total_sub} préstamos")
        total_categoria += total_sub
    print(f"  Total en {categoria}: {total_categoria} préstamos")
    total_general += total_categoria

print(f"\nTotal  semanal: {total_general} préstamos")
