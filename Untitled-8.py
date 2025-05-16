saldo = 1000  # saldo inicial
depositos = 0
retiros = 0

opcion = ""
edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]
turnos = ["Mañana", "Tarde", "Noche"]
dias = 7

# Crear matriz para guardar el consumo [edificio][día][turno]
consumo = [[[0 for _ in turnos] for _ in range(dias)] for _ in edificios]

# Ingreso de datos
for e in range(len(edificios)):
    print(f"\nEdificio: {edificios[e]}")
    for d in range(dias):
        for t in range(len(turnos)):
            while True:
                entrada = input(f"Día {d + 1}, turno {turnos[t]} (kWh): ")
                if entrada.replace('.', '', 1).isdigit():
                    consumo[e][d][t] = float(entrada)
                    break
                else:
                    print("⚠️ Ingrese un número válido.")

# Mostrar consumo por edificio
print("\n--- Consumo por edificio ---")
total_general = 0
for e in range(len(edificios)):
    total_edificio = 0
    for d in range(dias):
        total_edificio += sum(consumo[e][d])
    print(f"{edificios[e]}: {total_edificio:.2f} kWh")
    total_general += total_edificio

# Mostrar total general
print(f"\n--- Consumo total en la semana: {total_general:.2f} kWh ---")
