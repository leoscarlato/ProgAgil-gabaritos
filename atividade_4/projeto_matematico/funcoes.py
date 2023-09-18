# Implemente as funcoes de acordo com o enunciado
def soma(a:int, b:int) -> int:
    return a + b if a + b > 0 else 0

def subtracao(a:int, b:int) -> int:
    return a - b if a - b > 0 else 0

def divisao(a:int, b:int) -> int:
    return a / b if b != 0 else "Impossível dividir por zero!"

def somatoria(lista:list) -> int:
    return sum(lista)