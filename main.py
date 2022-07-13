import simulator as sm

c = sm.Circuit()

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, N0, N1, N2 = [
                            c.add_node() for i in range(15)
                            ]

c.add_v_source(19918.58, n1, N0)
c.add_v_source(sm.pol2rect(19918.58, -120), n5, N0)
c.add_v_source(sm.pol2rect(19918.58, -240), n9, N0)

# Impedancias Carga 1

c.add_impedance(5951.25, n2, N1)
c.add_impedance(5951.25, n6, N1)
c.add_impedance(5951.25, n10, N1)

# Impedancias Carga 2

c.add_impedance(14.69 + 1.83j, n3, N2)
c.add_impedance(23.88 - 11.94j, n7, N2)
c.add_impedance(9.55 + 4.77j, n11, N2)

# Impedancia Carga 3

c.add_impedance(1666.34+1700j, n4, n12)
c.add_impedance(1666.34+1700j, n4, n8)
c.add_impedance(1666.34 + 1700j, n8, n12)

# Impedancia líneas 5 km

c.add_impedance(0.5+0.05j, n1, n2)
c.add_impedance(0.5+0.05j, n5, n6)
c.add_impedance(0.5+0.05j, n9, n10)

# Impedancia línea 15 km

c.add_impedance(1.5+0.15j, n2, n3)
c.add_impedance(1.5+0.15j, n6, n7)
c.add_impedance(1.5+0.15j, n10, n11)

# Impedancia línea 25 km

c.add_impedance(2.5+0.25j, n3, n4)
c.add_impedance(2.5+0.25j, n7, n8)
c.add_impedance(2.5+0.25j, n11, n12)

c.solve()

# CORRIENTES DE LINEA
