import pytest
from Teste_contador.contador import count_letters_digits


def test_conta_somente_letras():
    resultado = count_letters_digits("abcXYZ")
    assert resultado == {"letras": 6, "digitos": 0}


def test_conta_somente_digitos():
    resultado = count_letters_digits("12345")
    assert resultado == {"letras": 0, "digitos": 5}


def test_conta_misturado():
    resultado = count_letters_digits("abc123")
    assert resultado == {"letras": 3, "digitos": 3}


def test_string_vazia():
    resultado = count_letters_digits("")
    assert resultado == {"letras": 0, "digitos": 0}
