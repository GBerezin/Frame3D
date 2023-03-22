# The Finite Element Method
# Georgy Berezin

import math
import Charts

# Import 'FEModel3D'  from 'PyNite'
from PyNite import FEModel3D
from prettytable import PrettyTable


def main():
    # Create a new model
    frame = FEModel3D()

    # Define the nodes
    frame.add_node('N1', 0, 0, 4)
    frame.add_node('N2', 2, 0, 4)
    frame.add_node('N3', 2, 0, 2)
    frame.add_node('N4', 2, 0, 0)
    frame.add_node('N5', 10, 0, 4)
    frame.add_node('N6', 13, 0, 0)

    # Define the supports
    frame.def_support('N4', True, True, True, True, True, True)
    frame.def_support('N6', True, True, True, False, False, False)

    # Add nodal loads
    frame.add_node_load('N1', 'FZ', -20, case='D')
    frame.add_node_load('N3', 'FX', 20, case='D')

    # Create members
    E = 1000

    J = 1
    Iz = 1
    G = 384.6154

    I1y = 20
    A1 = 200

    I2y = 10
    A2 = 100

    # 'Define the materials'
    frame.add_material('Concrete', E, G, 0.3, 0)

    frame.add_member('M12', 'N1', 'N2', 'Concrete',
                     I1y, Iz, J, A1, None, False, False)
    frame.add_member('M23', 'N2', 'N3', 'Concrete',
                     I2y, Iz, J, A2, None, False, False)
    frame.add_member('M34', 'N3', 'N4', 'Concrete',
                     I2y, Iz, J, A2, None, False, False)
    frame.add_member('M25', 'N2', 'N5', 'Concrete',
                     I1y, Iz, J, A1, None, False, False)
    frame.add_member('M56', 'N5', 'N6', 'Concrete',
                     I2y, Iz, J, A2, None, False, False)
    frame.add_member('M45', 'N4', 'N5', 'Concrete',
                     I2y, Iz, J, A2, None, False, False)

    # Release the moments at the ends of the members
    frame.def_releases('M23', False, False, False, False, True, False,
                       False, False, False, False, False, False)
    frame.def_releases('M45', False, False, False, False, True, False,
                       False, False, False, False, True, False)

    # live loads to the frame
    # Note that we could leave 'x1' and 'x2' undefined below and it would default to the full member length
    # Note also that the direction uses lowercase notations to indicate member local coordinate systems
    frame.add_member_dist_load(
        'M25', Direction='Fz', w1=-10, w2=-10, x1=0, x2=8, case='L')
    frame.add_member_dist_load(
        'M45', Direction='Fz', w1=-5, w2=-5, x1=0, x2=math.sqrt(4 ** 2 + 8 ** 2), case='L')
    frame.add_member_dist_load(
        'M45', Direction='Fx', w1=10, w2=10, x1=0, x2=math.sqrt(4 ** 2 + 8 ** 2), case='L')
    frame.add_member_dist_load('M56', Direction='Fz', w1=-10,
                               w2=-10, x1=0, x2=math.sqrt(4 ** 2 + 3 ** 2), case='L')

    # Create load combinations
    frame.add_load_combo('1.0D+1.0L', factors={'D': 1.0, 'L': 1.0})

    # Analyze the frame
    frame.analyze()
    print('Перемещения узлов:')
    pt = PrettyTable(["Node", "DX", "DZ", "RY"])
    for i in frame.Nodes:
        pt.add_row([i, frame.Nodes[i].DX['1.0D+1.0L'],
                   frame.Nodes[i].DZ['1.0D+1.0L'], frame.Nodes[i].RY['1.0D+1.0L']])
    print(pt)
    Charts.geom(frame, 'Геометрия')


if __name__ == '__main__':
    main()
