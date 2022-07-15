import simulator as sm
import calculos_iniciales as ci
# import numpy as np

c = sm.Circuit()

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, N0, N1, N2 = [

                    c.add_node() for i in range(15)

                    ]

genA = c.add_v_source(sm.pol2rect(ci.V_LN, 0), n1, N0)
genB = c.add_v_source(sm.pol2rect(ci.V_LN, -120), n5, N0)
genC = c.add_v_source(sm.pol2rect(ci.V_LN, -240), n9, N0)

# Impedancias Carga 1

c.add_impedance(ci.Z1_a, n2, N1)
c.add_impedance(ci.Z1_a, n6, N1)
c.add_impedance(ci.Z1_a, n10, N1)

# Impedancias Carga 2

c.add_impedance(ci.Z2_a, n3, N2)
c.add_impedance(ci.Z2_b, n7, N2)
c.add_impedance(ci.Z2_c, n11, N2)

# Impedancia Carga 3

c.add_impedance(ci.Z3_a, n4, n12)
c.add_impedance(ci.Z3_a, n4, n8)
c.add_impedance(ci.Z3_a, n8, n12)

# # Impedancia líneas 5 km
#
# faseA_5km = c.add_impedance(0.5+0.05j, n1, n2)
# faseB_5km = c.add_impedance(0.5+0.05j, n5, n6)
# faseC_5km = c.add_impedance(0.5+0.05j, n9, n10)
#
# # Impedancia línea 15 km
#
# faseA_15km = c.add_impedance(1.5+0.15j, n2, n3)
# faseB_15km = c.add_impedance(1.5+0.15j, n6, n7)
# faseC_15km = c.add_impedance(1.5+0.15j, n10, n11)
#
# # Impedancia línea 25 km
#
# faseA_25km = c.add_impedance(2.5+0.25j, n3, n4)
# faseB_25km = c.add_impedance(2.5+0.25j, n7, n8)
# faseC_25km = c.add_impedance(2.5+0.25j, n11, n12)

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

c.add_impedance(1e-20, N0, N1)
c.add_impedance(1e-20, N1, N2)

c.solve()

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

# print("\nCORRIENTES DE LÍNEA:")
# print("   Antes de la empresa 1:")
# print("      Fase A: ", I_A1)
# print("      Fase B: ", I_A2)
# print("      Fase C: ", I_A3)


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

# print("\nCORRIENTES DE LÍNEA:")
# print("   Antes de la empresa 2:")
# print("      Fase A: ", I2_A1)
# print("      Fase B: ", I2_A2)
# print("      Fase C: ", I2_A3)

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

# print("\nCORRIENTES DE LÍNEA:")
# print("   Antes de la empresa 2:")
# print("      Fase A: ", I3_A1)
# print("      Fase B: ", I3_A2)
# print("      Fase C: ", I3_A3)

"""
calculo de tensiones entre lineas
"""

# en la salida de la subestacion

vAB = c.measure_v(n5, n1)
vBC = c.measure_v(n9, n5)
vCA = c.measure_v(n1, n9)

# en la empresa 1

v1_a1 = c.measure_v(n2, n6)
v1_a2 = c.measure_v(n6, n10)
v1_a3 = c.measure_v(n2, n10)

# potencias

# S_carga1 = 3*v1_a1**2/ci.Z1_a
# S_source = genA*np.conj(I_A1)

a = [
     '\n**********************\n',
     'CORRIENTES DE LÍNEA:\n',
     '\n',
     'Antes de la empresa 1:\n',
     '    Fase A: {}\n'.format(I_A1),
     '    Fase B: {}\n'.format(I_A2),
     '    Fase C: {}\n'.format(I_A3),
     '\nAntes de la empresa 2:\n',
     '    Fase A: {}\n'.format(I2_A1),
     '    Fase B: {}\n'.format(I2_A2),
     '    Fase C: {}\n'.format(I2_A3),
     '\nAntes de la empresa 3:\n',
     '    Fase A: {}\n'.format(I3_A1),
     '    Fase B: {}\n'.format(I3_A2),
     '    Fase C: {}\n'.format(I3_A3),
     '\nTENSIONES ENTRE LINEAS:\n',
     '\n',
     'En la salida de la subestacion:\n',
     '    VAB: {}\n'.format(sm.rect2pol(vAB)),
     '    VAB: {}\n'.format(sm.rect2pol(vBC)),
     '    VAB: {}\n'.format(sm.rect2pol(vCA)),
     '\nAcometida de la empresa 1:\n',
     '    VA\'B\': {}\n'.format(sm.rect2pol(v1_a1)),
     '    VB\'C\': {}\n'.format(sm.rect2pol(v1_a2)),
     '    VC\'A\': {}\n'.format(sm.rect2pol(v1_a3))
     ]

with open('restults.txt', 'w') as f:
    for line in a:
        f.write(line)

with open('restults.txt', 'r') as fl:
    text = fl.read()
    print(text)
