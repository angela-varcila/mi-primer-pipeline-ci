import sys
from calculadora import sumar, restar, multiplicar, dividir
 
OPERACIONES = {
    "sumar": sumar,
    "restar": restar,
    "multiplicar": multiplicar,
    "dividir": dividir,
}
 
def main():
    if len(sys.argv) != 4:
        print("Uso: python main.py <operacion> <numero1> <numero2>")
        print("Operaciones: sumar, restar, multiplicar, dividir")
        raise SystemExit(1)
 
    operacion = sys.argv[1].lower()
    if operacion not in OPERACIONES:
        print(f"Operación no válida: {operacion}")
        raise SystemExit(1)
 
    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        resultado = OPERACIONES[operacion](a, b)
    except ValueError as error:
        print(f"Error: {error}")
        raise SystemExit(1)
 
    print(resultado)
 
if __name__ == "__main__":
    main()
