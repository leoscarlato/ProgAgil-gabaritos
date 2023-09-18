import pytest
from funcoes import soma, subtracao, divisao, somatoria

@pytest.mark.simples
def test_soma_positiva():
    assert soma(5, 3) == 8

@pytest.mark.simples
def test_soma_negativa():
    assert soma(3, -5) == 0

@pytest.mark.simples
def test_subtracao_resultado_positivo():
    assert subtracao(5, 3) == 2

@pytest.mark.simples
def test_subtracao_resultado_negativo():
    assert subtracao(3, 5) == 0

@pytest.mark.simples
def test_divisao():
    assert divisao(9, 3) == 3

@pytest.mark.simples
def test_divisao_por_zero():
    assert divisao(9, 0) == "Impossível dividir por zero!"

@pytest.mark.lista
def test_somatoria():
    assert somatoria([1,2,3,4,5,6,7,8,9,10]) == 55