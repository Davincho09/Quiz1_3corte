
objetos = [
    {'nombre': 'A', 'peso': 10, 'valor': 60},
    {'nombre': 'B', 'peso': 20, 'valor': 100},
    {'nombre': 'C', 'peso': 30, 'valor': 120}
]

capacidad = 50  

for obj in objetos:
    obj['relacion'] = obj['valor'] / obj['peso']

objetos.sort(key=lambda x: x['relacion'], reverse=True)
peso_total = 0
valor_total = 0
seleccion = []

for obj in objetos:
    if peso_total + obj['peso'] <= capacidad:
        peso_total += obj['peso']
        valor_total += obj['valor']
        seleccion.append({'objeto': obj['nombre'], 'fraccion': 1})
    else:
        restante = capacidad - peso_total
        fraccion = restante / obj['peso']
        valor_total += obj['valor'] * fraccion
        peso_total += obj['peso'] * fraccion
        seleccion.append({'objeto': obj['nombre'], 'fraccion': fraccion})
        break  

print("=== Resultado del algoritmo voraz ===")
for s in seleccion:
    print(f"Objeto {s['objeto']} -> {s['fraccion']*100:.1f}% tomado")

print(f"\nPeso total en la mochila: {peso_total:.2f} kg")
print(f"Valor total obtenido: {valor_total:.2f} monedas de oro")
