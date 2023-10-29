import matplotlib.pyplot as plt
from vec2 import Vec2
from numList import NumList
from itertools import combinations


def a(s, mG):
    """calculate the acceleration of each planet in a system"""   
    a = NumList(Vec2() for _ in s)      # initialise acceleration vectors to zero
    for (s1, mG1, a1), (s2, mG2, a2) in combinations(zip(s, mG, a), 2):
        s12 = s2 - s1
        f = s12 / pow(abs(s12), 3)      # 1/r^2 in the direction of s12
        a1 += f * mG2                   # acceleration of 1 due to 2 (f = ma)
        a2 -= f * mG1                   # acceleration of 2 due to 1
    return a


def main():
    """simulate the system and plot the results"""

    # ==================== initialisation ======================
    #
    dt = 60                     # simultion increment (sec)
    t_max = 27.3 * 24 * 60 * 60 # one lunar month is 27.3 days

    # gravitational constant (currently unused)
    G = 6.674e-11

    # masses (normally these would be multiplied by G)
    #
    mG = [
        5.97e24 * G,            # earth mass (kg)
        7.35e22 * G,            # moon mass (kg)
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
        ks_1 = a(s, mG)
        kv_1 = v
      
        ks_2 = a(s + kv_1 * (dt/2), mG)
        kv_2 = v + ks_1 * (dt/2)

        ks_3 = a(s + kv_2 * (dt/2), mG)
        kv_3 = v + ks_2 * (dt/2)

        ks_4 = a(s + kv_3 * dt, mG)
        kv_4 = v + ks_3 * dt

        # predict new displacements and velocities
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