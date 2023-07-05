import matplotlib.pyplot as plt
from vec2 import Vec2
from numList import NumList
from itertools import combinations


def a(s, mG):
    """Calculate the acceleration of each planet in a system due to gravitational attraction.
    s: position vectors
    mG: masses times G
    Returns: acceleration vectors"""
   
    a = NumList(Vec2() for _ in s)      # initialise acceleration vectors to zero

    # add up accelerations due to each pair of bodies
    #
    for i1, i2 in combinations(range(len(s)), 2):
        s12 = s[i2] - s[i1]             # displacement s1 -> s2
        f = s12 / pow(abs(s12), 3)      # 1/r^2 times the unit vector
        a[i1] += f * mG[i2]             # acceleration of 1 due to 2 (a = f/m)
        a[i2] -= f * mG[i1]             # acceleration of 2 due to 1

    return a


def main():

    # ==================== initialisation ======================
    #
    t = 0
    dt = 0.01
    t_max = 5

    # gravitational constant (currently unused)
    G = 6.67430e-11

    # masses (normally these should be multiplied by G)
    #
    mG = [
        1,
        1,
        1,
        1 
    ]

    # initial positions
    #
    s = NumList([
        Vec2( 0,  1),
        Vec2( 1,  0),
        Vec2( 0, -1),
        Vec2(-1,  0)
    ])

    # initial velocities
    #
    v = NumList([
        Vec2(-0.5,    0),
        Vec2(   0,  0.5),
        Vec2( 0.5,    0),
        Vec2(   0, -0.5)
    ])

    # initialise lists of coordinates
    #
    x_coords = [[] for _ in s]
    y_coords = [[] for _ in s]

    # ======================== main loop =========================
    # iterate solution and gather data for graph
    #
    while t <= t_max:

        # record results
        #
        for this_s, x_list, y_list in zip(s, x_coords, y_coords):
            x_list.append(this_s.x)
            y_list.append(this_s.y)

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
    
    # ==================== display results ======================
    #
    fig, ax = plt.subplots(1, 1)
    ax.set_title('Orbit Simulation')
    for x_list, y_list in zip(x_coords, y_coords):
        ax.plot(x_list, y_list)
    ax.set_aspect('equal', 'box')
    ax.grid()
    plt.show()

if __name__== '__main__':
    main()