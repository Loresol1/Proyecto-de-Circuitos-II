import numpy as np
import simulator as sim


def calculadora_impedancias(V, S):
    return V**2/np.conj(S)


def pot2imp(S, fp, VLL):
    """
    Recibe la potencia compleja en VA, el factor de potencia y la tensión entre
    lineas y devuelve el valor de la impedancia en ohms y en forma polar
    """
    P = S*fp
    Q = P*np.tan(np.arccos(fp))
    ST = P + 1j*Q

    return sim.rect2pol(VLL**2/np.conj(ST))


V_LL = 34.5e3

# Tensiones linea-neutro
V_LN = V_LL/np.sqrt(3)


"""
Calculos para la primera carga
"""

S1_total = 2000e3 + 0j
S1_carga = S1_total/3

Z1_a = calculadora_impedancias(V_LN, S1_carga)
print("Primera carga:")
print("   Fase A: {:.2f}".format(Z1_a))
print("   Fase B: {:.2f}".format(Z1_a))
print("   Fase C: {:.2f}".format(Z1_a))

"""
Calculos para la segunda carga
"""
S2_faseA = (4000+500j)*1e3
S2_faseB = (2000-1000j)*1e3
S2_faseC = (5000+2500j)*1e3

Z2_a = calculadora_impedancias(V_LN, S2_faseA)
Z2_b = calculadora_impedancias(V_LN, S2_faseB)
Z2_c = calculadora_impedancias(V_LN, S2_faseC)

print("Segunda carga:")
print("   Fase A: {:.2f}".format(Z2_a))
print("   Fase B: {:.2f}".format(Z2_b))
print("   Fase C: {:.2f}".format(Z2_c))

"""
Calculos para la tercera carga
"""
S3_mag = 1500*1e3
S3_angle = np.arccos(0.7)
P = S3_mag*np.cos(S3_angle)
Q = S3_mag*np.sin(S3_angle)
S3_total = P + Q*1j
S3_carga = S3_total/3

Z3_a = calculadora_impedancias(V_LL, S3_carga)

print("Tercera carga:")
print("   Fase A: {:.2f}".format(Z3_a))
print("   Fase B: {:.2f}".format(Z3_a))
print("   Fase C: {:.2f}".format(Z3_a))


print('**************************')
print('**Sea S=1500kVA y fp=0.7**')
print('**************************')
print('Z = {}'.format(pot2imp(1500*1e3, 0.7, V_LL)))
