import matplotlib.pyplot as plt
from vec2 import Vec2
from numList import NumList
from itertools import combinations

dt = 0.01
t_max = 5

#G = 6.67430e-11
G = 1


def a(s, mG):
    """Calculate the acceleration of each planet in a system due to gravitational attraction.
    s: position vectors
    mG: masses (times G)
    Returns: acceleration vectors"""

    n = len(s)    
    a = NumList(Vec2() for _ in range(n))       # initialise acceleration vectors to zero

    # iterate over each pair of array indices
    #
    for i1, i2 in combinations(range(n), 2):
        s12 = s[i2] - s[i1]             # displacement s1 -> s2
        f = s12 / pow(abs(s12), 3)      # 1/r^2 times the unit vector
        a[i1] += f * mG[i2]             # update a1 due to m2 (a = f/m)
        a[i2] -= f * mG[i1]             # update a2 due to m1

    return a


def a_old(s):
    """ acceleration at displacement s (vector) """
    k = mu / pow(abs(s), 3)
    a = Vec2( -k * s.x, -k * s.y)
    return a


def main():

    # initialisation
    #  
    t = 0               # initial time
    mG = [
        10 * G,
        1 * G
    ]
    s = NumList([
        Vec2(0, 0),
        Vec2(1, 0)
    ])
    v = NumList([
        Vec2(0, 0),
        Vec2(0, 4)
    ])

    # coordinates to be plotted
    #
    x0 = []
    y0 = []
    x1 = []
    y1 = []

    # iterate solution
    #
    while t <= t_max:

        # record results
        #
        x0.append(s[0].x)
        y0.append(s[0].y)
        x1.append(s[1].x)
        y1.append(s[1].y)

        # calculate RK coefficients for displacement and velocity
        #
        ks_1 = a(s, mG)
        kv_1 = v
      
        ks_2 = a(s + kv_1 * (dt/2), mG)
        kv_2 = v + ks_1 * (dt/2)

        ks_3 = a(s + kv_2 * (dt/2), mG)
        kv_3 = v + ks_2 * (dt/2)

        ks_4 = a(s + kv_3 * dt, mG)
        kv_4 = v + ks_3 * dt

        # predict new displacement and velocity
        #
        t += dt
        v = v + (dt/6) * (ks_1 + 2 * ks_2 + 2 * ks_3 + ks_4)
        s = s + (dt/6) * (kv_1 + 2 * kv_2 + 2 * kv_3 + kv_4)
    
    # display results
    #
    fig, ax = plt.subplots(1, 1)
    ax.set_title('Simulation')
    ax.scatter(x0, y0, marker='.')
    ax.scatter(x1, y1, marker='.')
    ax.set_aspect('equal', 'box')
    ax.grid()
    plt.show()

if __name__== '__main__':
    main()