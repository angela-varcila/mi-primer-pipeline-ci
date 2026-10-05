import pytest

from calculadora import sumar, restar, multiplicar, dividir, calcular_total


def test_sumar():
    assert sumar(2, 3) == 5


def test_restar():
    assert restar(8, 3) == 5


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_sumar_con_negativos():
    assert sumar(-4, -3) == -7

def test_restar_resultado_negativo():
    assert restar(3, 8) == -5

def test_multiplicar_por_cero():
    assert multiplicar(9, 0) == 0

def test_dividir_resultado_decimal():
    assert dividir(7, 2) == 3.5

#------ AQUI INCLUYO NUEVAS PRUEBAS ------
def test_sumar_positivo_negativo():
    assert sumar(5, -2) == 3

def test_restar_iguales():
    assert restar(5, 5) == 0

def test_multiplicar_negativos():
    assert multiplicar(-3, -2) == 6

def test_dividir_negativo_por_positivo():
    assert dividir(-10, 2) == -5.0


def test_calcular_total_con_descuento():
    assert calcular_total(50, 3, 10) == 135

#------ OTRAS PRUEBAS DE INTEGRACION ------
'''	Un caso sin descuento (0 %).
•	Una compra de una sola unidad con descuento.
•	Una compra con precio decimal y un descuento distinto al ejemplo.
•	Un caso con cantidad cero, definiendo y justificando el resultado esperado.'''

def test_calcular_total_sin_descuento():
    assert calcular_total(100, 2, 0) == 200

def test_calcular_total_una_unidad_con_descuento():
    assert calcular_total(80, 1, 15) == 68

def test_calcular_total_precio_decimal_descuento():
    assert calcular_total(19.99, 5, 20) == 79.96

def test_calcular_total_cantidad_cero():
    # Si la cantidad es cero, el total esperado es cero, ya que no se está comprando nada.
    assert calcular_total(50, 0, 10) == 0
  
