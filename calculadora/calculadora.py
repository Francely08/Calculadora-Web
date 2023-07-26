n1 = input("Ingrese primer número")
n2 = input("Ingrese el segundo número")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicar = n1 * n2
division = n1 / n2

mesaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma}.
el resulatado de la resta es {resta}.
el resultado de la multiplicación es {multiplicar}.
el resultado de la division es {division}.
"""

print(mesaje)