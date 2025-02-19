"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones


# Entradas

año = int(input("Introduzca un año: "))

# Proceso

if año % 4 == 0:
    salida = str(año) + " sí es un año bisiesto"

elif año % 400 == 0:
    salida = str(año) + " sí es un año bisiesto" 

else:
    salida = str(año) + " no es un año bisiesto"



# Salidas
print(salida)
