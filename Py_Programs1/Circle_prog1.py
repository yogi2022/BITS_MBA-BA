# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:56:27 2022

@author: YOGESH
"""

pi = 3.14159
def area(radius):
    return pi*(radius**2)
def circumference(radius):
    return 2*pi*radius
def sphereSurface(radius):
    return 4.0*area(radius)
def sphereVolume(radius):
    return (4.0/3.0)*pi*(radius**3)