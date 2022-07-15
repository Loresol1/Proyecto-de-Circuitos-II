import simulator as sm
import calculos_iniciales as ci
import numpy as np

c = sm.Circuit()


#n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, N0, N1, N2 = [c.add_node() for i in range(15)]
N0, n1, n5, n9, n2, n6, n10, n3, n7, n11, n4, n8, n12, = [c.add_node() for i in range(13)]

generadorA = c.add_v_source(sm.pol2rect(ci.V_LN, 0), n1, N0)
generadorB = c.add_v_source(sm.pol2rect(ci.V_LN, -120), n5, N0)
generadorC =c.add_v_source(sm.pol2rect(ci.V_LN, -240), n9, N0)

# Impedancias Carga 1

Z1A = c.add_impedance(ci.Z1_a, n2, N0)
Z1B = c.add_impedance(ci.Z1_a, n6, N0)
Z1C = c.add_impedance(ci.Z1_a, n10, N0)

# Impedancias Carga 2

Z2A = c.add_impedance(ci.Z2_a, n3, N0)
Z2B = c.add_impedance(ci.Z2_b, n7, N0)
Z2C = c.add_impedance(ci.Z2_c, n11, N0)

# Impedancia Carga 3

Z3A = c.add_impedance(ci.Z3_a, n4, n12)
Z3B = c.add_impedance(ci.Z3_a, n4, n8)
Z3C = c.add_impedance(ci.Z3_a, n8, n12)

# Impedancia lineas 5 km

faseA_5km = c.add_impedance(0.5+0.05j, n1, n2)
faseB_5km = c.add_impedance(0.5+0.05j, n5, n6)
faseC_5km = c.add_impedance(0.5+0.05j, n9, n10)

# Impedancia linea 15 km

faseA_15km = c.add_impedance(1+0.1j, n2, n3)
faseB_15km = c.add_impedance(1+0.1j, n6, n7)
faseC_15km = c.add_impedance(1+0.1j, n10, n11)

# Impedancia linea 25 km

faseA_25km = c.add_impedance(1+0.1j, n3, n4)
faseB_25km = c.add_impedance(1+0.1j, n7, n8)
faseC_25km = c.add_impedance(1+0.1j, n11, n12)

# Lineas de neutro

#c.add_impedance(1e-20, N0, N1)
#c.add_impedance(1e-20, N1, N2)

c.solve()
# print(c.A)
# for i in range(c.A.shape[0]):
#     print(f'Nodo {i+1}: {c.A[i,i]}')
#
# print(np.sum(np.abs(c.A)))
# print(c.b)
#
# exit()
def corrientes_de_linea():
    """
    Corrientes de linea antes de la empresa 1
    """

    ca_e1_faseA = c.measure_i(faseA_5km)
    ca_e1_faseB = c.measure_i(faseB_5km)
    ca_e1_faseC = c.measure_i(faseC_5km)

    I_A1 = sm.rect2pol(ca_e1_faseA)
    I_A1 = tuple([float("{0:.2f}".format(n)) for n in I_A1])

    I_A2 = sm.rect2pol(ca_e1_faseB)
    I_A2 = tuple([float("{0:.2f}".format(n)) for n in I_A2])

    I_A3 = sm.rect2pol(ca_e1_faseC)
    I_A3 = tuple([float("{0:.2f}".format(n)) for n in I_A3])

    print("\nCORRIENTES DE LINEA:")
    print("   Antes de la empresa 1:")

    print("      Fase A: ", I_A1)
    print("      Fase B: ", I_A2)
    print("      Fase C: ", I_A3)

    """
    Corrientes de linea antes de la empresa 2
    """

    ca_e2_faseA = c.measure_i(faseA_15km)
    ca_e2_faseB = c.measure_i(faseB_15km)
    ca_e2_faseC = c.measure_i(faseC_15km)

    I2_A1 = sm.rect2pol(ca_e2_faseA)
    I2_A1 = tuple([float("{0:.2f}".format(n)) for n in I2_A1])

    I2_A2 = sm.rect2pol(ca_e2_faseB)
    I2_A2 = tuple([float("{0:.2f}".format(n)) for n in I2_A2])

    I2_A3 = sm.rect2pol(ca_e2_faseC)
    I2_A3 = tuple([float("{0:.2f}".format(n)) for n in I2_A3])

    #print("\nCORRIENTES DE LINEA:")
    print("   Antes de la empresa 2:")

    print("      Fase A: ", I2_A1)
    print("      Fase B: ", I2_A2)
    print("      Fase C: ", I2_A3)

    """
    Corrientes de linea antes de la empresa 2
    """

    ca_e3_faseA = c.measure_i(faseA_25km)
    ca_e3_faseB = c.measure_i(faseB_25km)
    ca_e3_faseC = c.measure_i(faseC_25km)

    I3_A1 = sm.rect2pol(ca_e3_faseA)
    I3_A1 = tuple([float("{0:.2f}".format(n)) for n in I3_A1])

    I3_A2 = sm.rect2pol(ca_e3_faseB)
    I3_A2 = tuple([float("{0:.2f}".format(n)) for n in I3_A2])

    I3_A3 = sm.rect2pol(ca_e3_faseC)
    I3_A3 = tuple([float("{0:.2f}".format(n)) for n in I3_A3])

    #print("\nCORRIENTES DE LINEA:")
    print("   Antes de la empresa 3:")

    print("      Fase A: ", I3_A1)
    print("      Fase B: ", I3_A2)
    print("      Fase C: ", I3_A3)

def tensiones_entre_lineas():
    """
    Tension entre lineas para la salida de la subestacion
    """
    print("\nTENSIONES ENTRE LINEAS")

    """
    Tension entre lineas para la salida de empresa 1
    """
    V_LN_1AB = sm.rect2pol(c.measure_v(n2, n6))
    V_LN_1AB = tuple([float("{0:.2f}".format(n)) for n in V_LN_1AB])

    V_LN_1BC = sm.rect2pol(c.measure_v(n6, n10))
    V_LN_1BC = tuple([float("{0:.2f}".format(n)) for n in V_LN_1BC])

    V_LN_1AC = sm.rect2pol(c.measure_v(n2, n10))
    V_LN_1AC = tuple([float("{0:.2f}".format(n)) for n in V_LN_1AC])

    print("   Acometida para empresa 1:")
    print("      V_AB1: ", V_LN_1AB)
    print("      V_BC1: ", V_LN_1BC)
    print("      V_AC1: ", V_LN_1AC)

    """
    Tension entre lineas para la salida de empresa 2
    """
    V_LN_2AB = sm.rect2pol(c.measure_v(n3, n7))
    V_LN_2AB = tuple([float("{0:.2f}".format(n)) for n in V_LN_2AB])

    V_LN_2BC = sm.rect2pol(c.measure_v(n7, n11))
    V_LN_2BC = tuple([float("{0:.2f}".format(n)) for n in V_LN_2BC])

    V_LN_2AC = sm.rect2pol(c.measure_v(n3, n11))
    V_LN_2AC = tuple([float("{0:.2f}".format(n)) for n in V_LN_2AC])

    print("   Acometida para empresa 2:")
    print("      V_AB2: ", V_LN_2AB)
    print("      V_BC2: ", V_LN_2BC)
    print("      V_AC2: ", V_LN_2AC)

    """
    Tension entre lineas para la salida de empresa 3
    """
    V_LN_3AB = sm.rect2pol(c.measure_v(n4, n8))
    V_LN_3AB = tuple([float("{0:.2f}".format(n)) for n in V_LN_3AB])

    V_LN_3BC = sm.rect2pol(c.measure_v(n8, n12))
    V_LN_3BC = tuple([float("{0:.2f}".format(n)) for n in V_LN_3BC])

    V_LN_3AC = sm.rect2pol(c.measure_v(n4, n12))
    V_LN_3AC = tuple([float("{0:.2f}".format(n)) for n in V_LN_3AC])

    print("   Acometida para empresa 3:")
    print("      V_AB3: ", V_LN_3AB)
    print("      V_BC3: ", V_LN_3BC)
    print("      V_AC3: ", V_LN_3AC)

def calculo_potencias():
    # Potencia para generadores
    S_generadorA = c.measure_S(generadorA)
    S_generadorB = c.measure_S(generadorB)
    S_generadorC = c.measure_S(generadorC)

    # Potencia para empresa1
    S_1A = c.measure_S(Z1A)
    S_1B = c.measure_S(Z1B)
    S_1C = c.measure_S(Z1C)

    # Potencia para empresa2
    S_2A = c.measure_S(Z2A)
    S_2B = c.measure_S(Z2B)
    S_2C = c.measure_S(Z2C)

    # Potencia para empresa3
    S_3A = c.measure_S(Z3A)
    S_3B = c.measure_S(Z3B)
    S_3C = c.measure_S(Z3C)

    S_tot_generat = S_generadorA + S_generadorB + S_generadorC
    S_tot_carga1 = S_1A + S_1B + S_1C
    S_tot_carga2 = S_2A + S_2B + S_2C
    S_tot_carga3 = S_3A + S_3B + S_3C
    S_tot_por_cargas = S_tot_carga1 + S_tot_carga2 + S_tot_carga3

    print(sm.rect2pol(S_tot_generat))
    print(sm.rect2pol(S_tot_carga1))
    print(sm.rect2pol(S_tot_carga2))
    print(sm.rect2pol(S_tot_carga3))


corrientes_de_linea()
tensiones_entre_lineas()
calculo_potencias()


"""
DUDAS PARA FRANCISCO:
1. Ver impedancias de linea para cada carga
2. Determine la tension entre lineas a la salida de la subestacion, y en la
acometida de cada una de las empresas
3. Como calcular la perdida de potencia para cada empresa
4. Por que me da negativa la potencia de para la carga 2
5. Para la carga dos, es sumar
6. La carga 3 tiene una potencia reactiva de 1070kj, entonces los capacitores tienen que proveer -1070k?
"""
