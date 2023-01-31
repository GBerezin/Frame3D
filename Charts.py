import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


def geom(frame, name):
    """Геометрия."""

    f = frame
    fig = plt.figure(num=name)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('auto')
    for i in frame.Members:
        ax.plot([f.Members[i].i_node.X, f.Members[i].j_node.X], [f.Members[i].i_node.Y, f.Members[i].j_node.Y],
                zs=[f.Members[i].i_node.Z, f.Members[i].j_node.Z])
        ax.text((f.Members[i].i_node.X + f.Members[i].j_node.X) / 2,
                (f.Members[i].i_node.Y + f.Members[i].j_node.Y) / 2,
                (f.Members[i].i_node.Z + f.Members[i].j_node.Z) / 2, i, size=10, ha='center', c='green')
    for i in f.Nodes:
        ax.scatter(f.Nodes[i].X, f.Nodes[i].Y, f.Nodes[i].Z, color='red')
        ax.text(f.Nodes[i].X, f.Nodes[i].Y, f.Nodes[i].Z, i, size=10, ha='center', c='blue')

    plt.title(name, pad=20)
    ax.set_xlabel('X, м')
    plt.title(name, pad=20)
    ax.set_xlabel('X, м')
    ax.set_ylabel('Y, м')
    ax.set_zlabel('Z, м')
    plt.show()


if __name__ == '__main__':
    print(geom.__doc__)
    input('Press Enter:')
