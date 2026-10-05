def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def calcular_total(precio, cantidad, descuento):
    subtotal = multiplicar(precio, cantidad)
    valor_descuento = multiplicar(subtotal, descuento / 100)
    total = restar(subtotal, valor_descuento)
    return total