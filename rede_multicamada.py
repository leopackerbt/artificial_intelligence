
import numpy as np

# função de ativação
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

a = sigmoid(0.5)
b = sigmoidDerivada(a)

#implementação camada oculta (operação xor)
    
entradas = np.array([[0,0],
                    [0,1],
                    [1,0],
                    [1,1]])
    
saidas = np.array([[0],[1],[1],[0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   # pesos x1 / pesos x2
                   [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017], [-0.893], [0.148]])

epocas = 100  

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    # faz o dot unir os arrays entradas com o array pesos0
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    # calculo erro = respostaCorreta - respostaCalculada ou
    # somar os erros e dividir pela qtd de respostas
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(erroCamadaSaida)
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida