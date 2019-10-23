# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 07:41:41 2019

@author: Davor Cortés
"""
import complejos as c

def particula_en_una_recta(n, vi):
    """
    Retorna un vector de probabilidades P.
    Parametros:
        n: Número de puntos sobre la recta.
        vi: Vector de estado inicial.
    """
    P = [0 for i in range(n)]
    modulo_v = c.modulo_vector(vi)
    for i in range(n):
        P[i] = round((c.modulo(vi[i])/modulo_v)**2, 4)
    
    #Graficación de resultados

    return P

    

def calculadora_estadistica_observables(o, vi):
    """
    Retorna el valor eperado E y la varianza S del observable
    Parametros:
        o: observable.
        vi: vector de estado inicial.
    """
    E, S = 0, 0
    
    #Normalizar el ket o vector inicial
    modulo_v = c.modulo_vector(vi)
    vi = c.vector_x_escalar(vi, 1/modulo_v)
    
    
    
    
    
    
