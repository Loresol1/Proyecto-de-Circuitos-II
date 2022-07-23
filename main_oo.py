import simulator as sm
import calculos_iniciales as ci


c = sm.Circuit()

N0, n1, n5, n9, n2, n6, n10, n3, n7, n11, n4, n8, n12, = [

                                c.add_node() for i in range(13)

                                ]

# Adicion Generador
generadorA = c.add_v_source(sm.pol2rect(ci.V_LN, 0), n1, N0)
generadorB = c.add_v_source(sm.pol2rect(ci.V_LN, -120), n5, N0)
generadorC = c.add_v_source(sm.pol2rect(ci.V_LN, -240), n9, N0)

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

c.solve()


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

    # print("\nCORRIENTES DE LINEA:")
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

    # print("\nCORRIENTES DE LINEA:")
    print("   Antes de la empresa 3:")

    print("      Fase A: ", I3_A1)
    print("      Fase B: ", I3_A2)
    print("      Fase C: ", I3_A3)


def tensiones_entre_lineas():
    """
    Tension entre lineas para la salida de la subestacion
    """
    # print("\nTENSIONES ENTRE LINEAS")

    V_subest_AB = sm.rect2pol(c.measure_v(n1, n5))
    V_subest_AB = tuple([float("{0:.2f}".format(n)) for n in V_subest_AB])

    V_subest_BC = sm.rect2pol(c.measure_v(n5, n9))
    V_subest_BC = tuple([float("{0:.2f}".format(n)) for n in V_subest_BC])

    V_subest_AC = sm.rect2pol(c.measure_v(n1, n9))
    V_subest_AC = tuple([float("{0:.2f}".format(n)) for n in V_subest_AC])

    print("   Tensiones a la salida de la subestacion:")
    print("      V_AB1: ", V_subest_AB)
    print("      V_BC1: ", V_subest_BC)
    print("      V_AC1: ", V_subest_AC)

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

    # Perdida de potencia en impedancias de linea de 5km
    S_5kmA = c.measure_S(faseA_5km)
    S_5kmB = c.measure_S(faseB_5km)
    S_5kmC = c.measure_S(faseC_5km)

    # Perdida de potencia en impedancias de linea de 15km
    S_15kmA = c.measure_S(faseA_15km)
    S_15kmB = c.measure_S(faseB_15km)
    S_15kmC = c.measure_S(faseC_15km)

    # Perdida de potencia en impedancias de linea de 25km
    S_25kmA = c.measure_S(faseC_25km)
    S_25kmB = c.measure_S(faseC_25km)
    S_25kmC = c.measure_S(faseC_25km)

    print("\nPERDIDA DE POTENCIA POR LINEAS")
    print("   Tramo antes de la empresa 1 (5 km):")
    print("      Carga A: {:.2f}" .format(S_5kmA))
    print("      Carga B: {:.2f}" .format(S_5kmB))
    print("      Carga C: {:.2f}" .format(S_5kmC))

    print("   Tramo antes de la empresa 1 (15 km):")
    print("      Carga A: {:.2f}".format(S_15kmA))
    print("      Carga B: {:.2f}".format(S_15kmB))
    print("      Carga C: {:.2f}".format(S_15kmC))

    print("   Tramo antes de la empresa 1 (25 km):")
    print("      Carga A: {:.2f}".format(S_25kmA))
    print("      Carga B: {:.2f}".format(S_25kmB))
    print("      Carga C: {:.2f}".format(S_25kmC))


def calcular_z():
    comp_Z2A = c.compensate(Z2A)
    comp_Z2B = c.compensate(Z2B)
    comp_Z2C = c.compensate(Z2C)

    comp_Z3A = c.compensate(Z3A)
    comp_Z3B = c.compensate(Z3B)
    comp_Z3C = c.compensate(Z3C)

    c.solve()

    def voltage_comparison():
        newV_LN_1AB = sm.rect2pol(c.measure_v(n2, n6))
        newV_LN_1AB = tuple([float("{0:.2f}".format(n)) for n in newV_LN_1AB])

        newV_LN_1BC = sm.rect2pol(c.measure_v(n6, n10))
        newV_LN_1BC = tuple([float("{0:.2f}".format(n)) for n in newV_LN_1BC])

        newV_LN_1AC = sm.rect2pol(c.measure_v(n2, n10))
        newV_LN_1AC = tuple([float("{0:.2f}".format(n)) for n in newV_LN_1AC])

        newV_LN_2AB = sm.rect2pol(c.measure_v(n3, n7))
        newV_LN_2AB = tuple([float("{0:.2f}".format(n)) for n in newV_LN_2AB])

        newV_LN_2BC = sm.rect2pol(c.measure_v(n7, n11))
        newV_LN_2BC = tuple([float("{0:.2f}".format(n)) for n in newV_LN_2BC])

        newV_LN_2AC = sm.rect2pol(c.measure_v(n3, n11))
        newV_LN_2AC = tuple([float("{0:.2f}".format(n)) for n in newV_LN_2AC])

        newV_LN_3AB = sm.rect2pol(c.measure_v(n3, n7))
        newV_LN_3AB = tuple([float("{0:.2f}".format(n)) for n in newV_LN_3AB])

        newV_LN_3BC = sm.rect2pol(c.measure_v(n7, n11))
        newV_LN_3BC = tuple([float("{0:.2f}".format(n)) for n in newV_LN_3BC])

        newV_LN_3AC = sm.rect2pol(c.measure_v(n3, n11))
        newV_LN_3AC = tuple([float("{0:.2f}".format(n)) for n in newV_LN_3AC])

        print("\nINCREMENTO DE FACTOR DE POTENCIA:")
        print("   Impedancias necesarias para incrementar el factor de"
              "   \n   potencia a 1:")

        print("      Carga 1: La carga 1 es puramente resistiva.")
        print("      Carga 2:")
        print("         Fase A: {:.2f}"  .format(comp_Z2A.value))
        print("         Fase B: {:.2f}"  .format(comp_Z2B.value))
        print("         Fase C: {:.2f}"  .format(comp_Z2C.value))
        print("      Carga 3:")
        print("         Fase A: {:.2f}".format(comp_Z3A.value))
        print("         Fase B: {:.2f}".format(comp_Z3B.value))
        print("         Fase C: {:.2f}".format(comp_Z3C.value))

        print("\nCOMPARACION DE TENSIONES:")
        print("   TENSIONES CON F.P CORREGIDO")
        print("      Empresa 1:")
        print("         V_AB1:", newV_LN_1AB)
        print("         V_BC1:", newV_LN_1BC)
        print("         V_AC1:", newV_LN_1AC)

        print("      Empresa 2:")
        print("         V_AB2:", newV_LN_2AB)
        print("         V_BC2:", newV_LN_2BC)
        print("         V_AC2:", newV_LN_2AC)

        print("      Empresa 3:")
        print("         V_AB3:", newV_LN_3AB)
        print("         V_BC3:", newV_LN_3BC)
        print("         V_AC3:", newV_LN_3AC)

    def S_comparison():
        new_S_5kmA = c.measure_S(faseA_5km)
        new_S_5kmB = c.measure_S(faseB_5km)
        new_S_5kmC = c.measure_S(faseC_5km)

        new_S_15kmA = c.measure_S(faseA_15km)
        new_S_15kmB = c.measure_S(faseB_15km)
        new_S_15kmC = c.measure_S(faseC_15km)

        new_S_25kmA = c.measure_S(faseA_25km)
        new_S_25kmB = c.measure_S(faseB_25km)
        new_S_25kmC = c.measure_S(faseC_25km)

        print("\nPERDIDA DE POTENCIA POR LINEAS")
        print("   Tramo antes de la empresa 1 (5 km):")
        print("      Carga A: {:.2f}".format(new_S_5kmA))
        print("      Carga B: {:.2f}".format(new_S_5kmB))
        print("      Carga C: {:.2f}".format(new_S_5kmC))

        print("   Tramo antes de la empresa 1 (15 km):")
        print("      Carga A: {:.2f}".format(new_S_15kmA))
        print("      Carga B: {:.2f}".format(new_S_15kmB))
        print("      Carga C: {:.2f}".format(new_S_15kmC))

        print("   Tramo antes de la empresa 1 (25 km):")
        print("      Carga A: {:.2f}".format(new_S_25kmA))
        print("      Carga B: {:.2f}".format(new_S_25kmB))
        print("      Carga C: {:.2f}".format(new_S_25kmC))

    voltage_comparison()
    S_comparison()


corrientes_de_linea()
tensiones_entre_lineas()
calculo_potencias()
calcular_z()
