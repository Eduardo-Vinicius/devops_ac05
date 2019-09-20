import pytest
from com.eduardodavi.converte_hora import converteHora

def test_hora():
	converte_hora = converteHora()
	assert (converte_hora.converte_hora([12,30]) == '12:30 PM', "Should be 12:30 PM")
    
def test_hora():
	converte_hora = converteHora()
	assert (converteHora.converte_hora([43,30]) == 'Erro!' , "Insira um valor válido")