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

def esperanza(o, vi):
    """
    Retorna la esperanza de un observable
    Parametros:
        o: observable.
        vi: vector de estado inicial.
    """
    #Normalizar el ket o vector inicial
    modulo_v = c.modulo_vector(vi)
    normalizado = c.vector_x_escalar(vi, 1/modulo_v)
    vec = c.accion_matriz_vector(o, normalizado)
    return (c.producto_interno_vectores(normalizado, vec))[0][0]

def varianza(o, vi):
    """
    Retorna la varianza de un observable
    Parametros:
        o: observable.
        vi: vector de estado inicial.
    """
    E = esperanza(o, vi)
    
    #Normalizar el ket o vector inicial
    modulo_v = c.modulo_vector(vi)
    normalizado = c.vector_x_escalar(vi, 1/modulo_v)
    
    temp = c.matriz_x_escalar(c.identidad(len(o)), E)
    temp = c.resta_de_matrices(o, temp)
    cuadrada = c.multiplicar_matrices_complejas(temp, temp)
    return esperanza(cuadrada, normalizado)

def estadisticas_observable(o, vi):
    """
    Retorna el valor eperado E y la varianza S del observable
    Parametros:
        o: observable.
        vi: vector de estado inicial.
    """
    E = esperanza(o, vi)

    if(c.es_hermitiana(o)):
        S = varianza(o, vi)
        
    return round(E, 1), round(S, 2)

    
    
    
    
    
    
    
    
    
