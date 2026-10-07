# Caleb Dorado NC = 0039

print("Ejemplos condiciones if 0039")

# Ejemplo 1: Verificar mayoria de edad
edad = 20
if edad >= 18:
    print("Acceso concedido: Eres mayor de edad.")

# Ejemplo 2:
usuario_activo = True
if usuario_activo:
    print("Bienvenido de nuevo al sistema.")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Ejemplos if elif 0039")

# Ejemplo 1: Calificaciones
puntuacion = 85
if puntuacion >= 90:
    print("Calificación: Excelente (A)")
elif puntuacion >= 80:
    print("Calificación: Buena (B)")
elif puntuacion >= 70:
    print("Calificación: Aceptable (C)")
elif puntuacion >= 60:
    print("Calificación: Apenas pasaste (D)")
elif puntuacion < 60:
    print("Calificación: Reprobado")

# Ejemplo 2: Categoria por edad
edad = 15
if edad < 13:
    print("Categoría: Niño")
elif edad < 20:
    print("Categoría: Adolescente")
elif edad <= 65:
    print("Categoría: Adulto")
elif edad > 65:
    print("Categoría: Mayor de edad")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Ejemplos if else 0039")

# Ejemplo 1:
numero = 7
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Ejemplo 2:
tiene_ticket = False
if tiene_ticket:
    print("Puedes ingresar a la función.")
else:
    print("Por favor, adquiere tu entrada en taquilla.")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Ejemplos for loops 0039")

# Ejemplo 1:
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta disponible: {fruta}")

# Ejemplo 2:
for i in range(1, 6):
    print(f"Paso número: {i}")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Ejemplos while loops 0039")

# Ejemplo 1:
contador = 1
while contador <= 4:
    print(f"Contador en: {contador}")
    contador += 1

# Ejemplo 2:
porcentaje = 0

while porcentaje < 100:
    porcentaje += 25
    print(f"Descargando... {porcentaje}%")
print("¡Descarga completada!")

print("Hecho por Caleb Dorado NC = 0039")