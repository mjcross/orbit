import matplotlib.pyplot as plt
from vec2 import Vec2
from numList import NumList
from itertools import combinations

DEBUG = False


def a(s, m):
    """calculate the accelerations of the planets due to gravitational attraction"""
    # gravitational constant
    G = 6.674e-11

    a = NumList(Vec2() for _ in s)          # initialise accumulated acceleration vectors to zero

    # iterate through pairs of planets and accumulate the accelerations
    #
    for (s1, m1, a1), (s2, m2, a2) in combinations(zip(s, m, a), 2):
        # s     position vectors
        # m     masses
        # a     acceleration vectors
        s12 = s2 - s1                       # displacement (vector)
        r = abs(s12)                        # magnitude of displacement (Vec2 class overloads 'abs()')
        u12 = s12 / r                       # direction of displacement (unit vector)
        f = (G * m1 * m2 / r ** 2) * u12    # force due to gravity (vector)
        a1 += f / m1                        # accumulate acceleration of 1 due to 2 (vector)
        a2 -= f / m2                        # accumulate acceleration of 2 due to 1 (vector)
    return a


def main():
    """simulate the system and plot the results"""

    # ==================== initialisation ======================
    #
    dt = 60                     # simultion increment (sec)
    t_max = 27.3 * 24 * 60 * 60 # one lunar month is 27.3 days


    # masses
    #
    m = [
        5.97e24,                # earth mass (kg)
        7.35e22,                # moon mass (kg)
    ]

    # initial positions
    #
    s = NumList([
        Vec2( 0,  0),
        Vec2( 3.631e8,  0),     # moon closest approach to earth (m)
    ])

    # initial velocities
    #
    v = NumList([
        Vec2(0,    0),
        Vec2(   0,  1082),      # moon maximum orbital velocity (ms-1)    
    ])

    # initialise lists of coordinates
    #
    x_coords = [[] for _ in s]
    y_coords = [[] for _ in s]

    # ======================== main loop =========================
    # iterate solution and gather data for graph
    #
    t = 0
    while t <= t_max:

        # record results
        #
        for this_s, x_list, y_list in zip(s, x_coords, y_coords):
            x_list.append(this_s.x)
            y_list.append(this_s.y)

        # calculate RK coefficients for displacement (ks_) and velocity (kv_)
        # (note that all the variables here are lists of vectors)
        #
        ks_1 = a(s, m)
        kv_1 = v
      
        ks_2 = a(s + kv_1 * (dt/2), m)
        kv_2 = v + ks_1 * (dt/2)

        ks_3 = a(s + kv_2 * (dt/2), m)
        kv_3 = v + ks_2 * (dt/2)

        ks_4 = a(s + kv_3 * dt, m)
        kv_4 = v + ks_3 * dt


        # predict changes in position and velocity
        #
        dv = (dt/6) * (ks_1 + 2*ks_2 + 2*ks_3 + ks_4)
        ds = (dt/6) * (kv_1 + 2*kv_2 + 2*kv_3 + kv_4)


        if DEBUG:
            # show intermediate values
            #
            print(f"Time:{t}")
            for i in range(2):
                print(f"\tplanet: {i}")
                print(f'\t\tposition {s[i]}')
                print(f'\t\tvelocity {v[i]}')
                print(f'\n\t\tks_1     {ks_1[i]}\n\t\tkv_1     {kv_1[i]}')
                print(f'\n\t\tks_2     {ks_2[i]}\n\t\tkv_2     {kv_2[i]}')
                print(f'\n\t\tks_3     {ks_3[i]}\n\t\tkv_3     {kv_3[i]}')
                print(f'\n\t\tks_4     {ks_4[i]}\n\t\tkv_4     {kv_4[i]}')
                print(f'\n\t\tdv       {dv[i]}')
                print(f'\t\tds       {ds[i]}')
                print()
                  
        # update positions and velocities
        #
        t += dt
        v = v + dv
        s = s + ds
    
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