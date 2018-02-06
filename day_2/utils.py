'''
Created on 06/02/2018

@author: asus
'''

def is_number(valor):
    """
    param: any Value
    return: int if valor is integer
    """
    
    try:
        return int(valor)
    except:
        return None

def is_float(valor):
    """
    param: any Value
    return: float if valor is real
    """
    
    try:
        return float(valor)
    except:
        return None