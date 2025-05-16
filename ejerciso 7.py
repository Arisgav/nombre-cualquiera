# Definir 
kioscos = 3
productos = 5
dias = 4

#  lista con los nombres de productos
nombres_productos = ["Galletas", "Agua", "Jugo", "Papas", "Chicle"]

#  [kiosco][producto][día]
ventas = [[[0 for _ in range(dias)] for _ in range(productos)] for _ in range(kioscos)]

# Ingreso de datos
for k in range(kioscos):
    print(f"\nKiosco {k + 1}")
    for p in range(productos):
        for d in range(dias):
            cantidad = int(input(f"Ventas de {nombres_productos[p]} - Día {d + 1}: "))
            ventas[k][p][d] = cantidad

# Mostrar total vendido por producto en cada kiosco
print("\n--- Total vendido por producto en cada kiosco ---")
for k in range(kioscos):
    print(f"\nKiosco {k + 1}")
    for p in range(productos):
        total_producto = sum(ventas[k][p])
        print(f"{nombres_productos[p]}: {total_producto} unidades")

# Mostrar total general vendido por día
print("\n--- Total general vendido por día ---")
for d in range(dias):
    total_dia = 0
    for k in range(kioscos):
        for p in range(productos):
            total_dia += ventas[k][p][d]
    print(f"Día {d + 1}: {total_dia} unidades vendidas")

