import numpy as np

def AND(x1, x2): #AND GATE
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp < 1:
        return 0
    else:
        return 1

def NAND(x1, x2): #NAND GATE
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp < 1:
        return 1
    else:
        return 0

def OR(x1, x2): #OR GATE
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = 0.5
    tmp = np.sum(w*x) + b
    if tmp >= 1:
        return 1
    else:
        return 0

def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    y = AND(s1, s2)
    return y




