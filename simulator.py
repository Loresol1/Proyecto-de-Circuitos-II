'''

    Este programa permite simular circuitos de corriente alterna que se
    componen de impedancias y fuentes independientes ideales.

    El programa fue diseñado y escrito por Francisco Escobar Prado para IE0309.
    Por favor reportar errores o puntos de mejora a
    francisco.escobarprado@ucr.ac.cr.

'''

import numpy as np


class Node:
    '''
    Clase para almacenar información de nodos.
    '''

    def __init__(self):

        self.voltage = 0        # Tensión del nodo
    # La tensión anterior se da con respecto a una tierra que es elegida por
    # el método solve de la clase Circuit. Este atributo voltage no debería
    # usarse externamente, sino que todas las tensiones deberían ser medidas
    # de forma diferencial con el método measure_v de abajo.


class Impedance:
    '''
    Clase para almacenar información de impedancias.
    '''

    def __init__(self, value, node_a, node_b):

        self.value = value      # Valor de la impedancia
        self.node_a = node_a    # Uno de los nodos
        self.node_b = node_b    # El otro
        # La distinción entre los dos nodos anteriores solo sirve para medir
        # la corriente de una forma no ambigua (véase el método get_current de
        # abajo).

    def get_voltage(self):
        '''
        Obtener tensión entre terminales de la impedancia (positivo en nodo a).
        '''

        return self.node_a.voltage - self.node_b.voltage

    def get_current(self):
        '''
        Obtener corriente a través de la impedancia (entrando por nodo a).
        '''

        return self.get_voltage()/self.value


class V_source:
    '''
    Clase para las fuentes independientes de tensión.
    '''

    def __init__(self, value, node_plus, node_minus):

        self.value = value              # Valor de la fuente
        self.node_plus = node_plus      # Nodo con el positivo
        self.node_minus = node_minus    # Nodo con el negativo
        self.current = 0                # Corriente inicializada como 0

    def get_voltage(self):
        '''
        Obtener tensión provista por la fuente (conocida a priori).
        '''

        return self.value

    def get_current(self):
        '''
        Obtener corriente a través de la fuente (incógnita, sale por el nodo +)
        '''

        return self.current


class I_source:
    '''
    Clase para las fuentes independientes de corriente.
    '''

    def __init__(self, value, node_tip, node_tail):

        self.value = value              # Valor de la fuente
        self.node_tip = node_tip        # Terminal de la que sale la corriente
        self.node_tail = node_tail      # Terminal en la que entra la corriente

    def get_voltage(self):
        '''
        Obtener tensión entre terminales de la fuente (incógnita, con + en tip)
        '''

        return self.node_tip.voltage - self.node_tail.voltage

    def get_current(self):
        '''
        Obtener corriente provista por la fuente (conocida a priori).
        '''

        return self.value


class Circuit:
    '''
    Clase asociada a un circuito.
    '''

    def __init__(self):

        # Listas para almacenar instancias de las otras clases
        self.nodes = []
        self.impedances = []
        self.v_sources = []
        self.i_sources = []

    def add_node(self):
        '''
        Agregar nodo al circuito.
        '''

        n = Node()
        self.nodes.append(n)

        return n

    def add_impedance(self, value, node_a, node_b):
        '''
        Agregar impedancia al circuito.
        '''

        z = Impedance(value, node_a, node_b)
        self.impedances.append(z)

        return z

    def add_v_source(self, value, node_plus, node_minus):
        '''
        Agregar fuente de tensión independiente al circuito.
        '''

        source = V_source(value, node_plus, node_minus)
        self.v_sources.append(source)

        return source

    def add_i_source(self, value, node_tip, node_tail):
        '''
        Agregar fuente de corriente independiente al circuito.
        '''

        source = I_source(value, node_tip, node_tail)
        self.i_sources.append(source)

        return source

    def node2ind(self, node):
        '''
        Obtener índice asociado a un nodo.

        La resta de -1 significa que el primer nodo definido siempre es tomado
        por el simulador como la tierra. Esto no reviste ninguna importancia
        porque las tensiones siempre se miden de forma diferencial (véase el
        método measure_v de abajo).
        '''

        return self.nodes.index(node) - 1

    def solve(self):
        '''
        Resolver circuito.

        Este método actualiza los siguientes atributos:

        - voltage, para los nodos,
        - current, para las fuentes de tensión.

        Si llamar al método arroja un error (generalmente de que la matriz A
        es singular), el circuito no fue especificado correctamente. Esto suele
        pasar porque se dejan nodos aislados o porque se conectan fuentes de
        tensión en paralelo o de corriente en serie.
        '''

        N = len(self.nodes)
        F = len(self.v_sources)

        # Inicializar matriz b (la mayoría de las entradas quedará así)
        b = np.zeros([N - 1 + F, 1], dtype=np.complex_)

        # Agregar términos a b debidos a fuentes de tensión
        if F > 0:
            b[-F:, 0] = [source.value for source in self.v_sources]

        # Agregar términos a b debidos a fuentes de corriente
        for source in self.i_sources:
            i = self.node2ind(source.node_tip)
            j = self.node2ind(source.node_tail)
            # Solo se agregan los términos si el nodo no es tierra (-1)
            if i != -1:
                b[i, 0] += source.value
            if j != -1:
                b[j, 0] -= source.value

        # Inicializar A
        A = np.zeros([N - 1 + F, N - 1 + F], dtype=np.complex_)

        # Agregar términos a A debidos a las impedancias
        for z in self.impedances:
            i = self.node2ind(z.node_a)
            j = self.node2ind(z.node_b)
            if i == -1:
                A[j, j] += 1.0/z.value
            elif j == -1:
                A[i, i] += 1.0/z.value
            else:
                A[i, i] += 1.0/z.value
                A[j, j] += 1.0/z.value
                A[i, j] -= 1.0/z.value
                A[j, i] -= 1.0/z.value

        # Agregar términos a A debidos a las fuentes de tensión
        for k, vs in enumerate(self.v_sources):
            i = self.node2ind(vs.node_plus)
            j = self.node2ind(vs.node_minus)
            if i != -1:
                A[i, N - 1 + k] = -1    # LCK
                A[N - 1 + k, i] = 1     # LTK
            if j != -1:
                A[j, N - 1 + k] = 1     # LCK
                A[N - 1 + k, j] = -1    # LTK

        # Resolver circuito
        x = np.linalg.solve(A, b)

        # Guardar tensiones nodales
        for i, n in enumerate(self.nodes[1:]):
            n.voltage = x[i, 0]

        # Guardar corrientes a través de fuentes de tensión
        for i, i_s in enumerate(x[-F:, 0]):
            self.v_sources[i].current = i_s

    def measure_v(self, node_plus, node_minus):
        '''
        Medir tensión entre dos nodos.
        '''

        return node_plus.voltage - node_minus.voltage

    def measure_i(self, element):
        '''
        Medir corriente a través de elemento según dirección de get_current.
        '''

        return element.get_current()

    def measure_S(self, element):
        '''
        Medir potencia (consumida para impedancias y generada para fuentes).
        '''

        return element.get_voltage()*np.conj(element.get_current())

    def compensate(self, Z):
        S = 1/np.conj(Z.value)
        S_comp = -1j * S.imag
        Z_comp = 1/np.conj(S_comp)

        return self.add_impedance(Z_comp, Z.node_a, Z.node_b)


def pol2rect(mag, degs):
    '''
    Definir número complejo a partir de magnitud y ángulo en grados.
    '''

    rads = np.deg2rad(degs)
    real = mag*np.cos(rads)
    imag = mag*np.sin(rads)

    return real + 1j*imag


def rect2pol(z):
    '''
    Obtener magnitud y ángulo en grados de un número complejo.
    '''

    mag = np.abs(z)
    rads = np.angle(z)
    degs = np.rad2deg(rads)

    return mag, degs
