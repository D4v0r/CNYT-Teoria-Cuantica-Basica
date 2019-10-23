# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:41:10 2019

@author: Davor Cortés
"""
import unittest
import funciones as f

class Test_funciones(unittest.TestCase):
    def test_particula_en_una_recta(self):
        n = 10
        vi = [(2,-1), (-1.5, 2.5), (-3.5, 5), (-4,6), (-3.5, 2.5), (0,0), (-3.5, 2.5), (6,-4), (0, 2.5), (-1, 1)]
        esperado = [0.025, 0.0425, 0.1862, 0.26, 0.0925, 0.0, 0.0925, 0.26, 0.0312, 0.01]
        self.assertEquals(f.particula_en_una_recta(n, vi), esperado)


if __name__ == "__main__":
    unittest.main()
