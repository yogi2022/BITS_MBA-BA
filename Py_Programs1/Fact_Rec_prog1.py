# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:58:37 2022

@author: YOGESH
"""

def factR(n):
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

factR(4)