# Quiz1_3corte
# Problema de la Mochila Fraccional (Algoritmo Voraz)

## 📘 Descripción
Un aventurero tiene una mochila que puede soportar hasta 50 kg.  
En el camino encuentra los siguientes objetos:

| Objeto | Peso (kg) | Valor (Monedas de Oro) | Valor/Peso |
|:------:|:----------:|:----------------------:|:-----------:|
| A | 10 | 60 | 6 |
| B | 20 | 100 | 5 |
| C | 30 | 120 | 4 |

El objetivo de este ejercicio es maximizar el valor total sin exceder los 50 kg utilizando un algoritmo voraz (greedy).

## Paso 1: Ordenar por relación valor/peso
Orden de prioridad (de mayor a menor)

1. A → 6  
2. B → 5  
3. C → 4  

## Paso 2: Aplicar el algoritmo voraz

Se agregan los objetos en orden hasta llenar la mochila

1. A → peso 10 kg → valor 60  
   Peso acumulado = 10 kg  
   Valor acumulado = 60  

2. B → peso 20 kg → valor 100  
   Peso acumulado = 30 kg  
   Valor acumulado = 160  

3. Quedan 20 kg de capacidad (50 - 30 = 20) 
   ⅔ del objeto C  
   Valor fraccional = (20/30) × 120 = 80  

## Resultado final

| Objeto | Cantidad | Valor aportado |
|:-------|:----------|:---------------|
| A | 1 | 60 |
| B | 1 | 100 |
| C | 2/3 | 80 |
| **Total** | — | **240 monedas de oro** |

**Valor máximo = 240 monedas de oro**


El aventurero debe llevar:
- Todo el objeto A
- Todo el objeto B
- Solo 2/3 del objeto C

De esta forma obtiene 240 monedas de oro sin exceder la capacidad de 50 kg.

