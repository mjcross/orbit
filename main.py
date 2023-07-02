import matplotlib.pyplot as plt
from vec2 import Vec2

mu = 132712440042e9     # standard gravitational parameter of the sun (m3/s2)
r_perihelion = 147100e6 # orbit radius of earth at perihelion (m)
v_perihelion = 30.29e3  # average orbital velocity (m/s)

v0 = Vec2(v_perihelion, 0)     # initial velocity vector
s0 = Vec2(0, r_perihelion)     # initial position vector

dt = 24 * 60 * 60       # 1 day
t_max = 365 * dt        # 1 year (approx)

def a(s):
    """ acceleration at displacement s (vector) """
    k = mu / pow(abs(s), 3)
    a = Vec2( -k * s.x, -k * s.y)
    return a


def main():
    # initialisation
    #  
    t = 0               # initial time
    v = v0              # initial velocity vector
    s = s0              # initial displacement vector

    # create list of coordinates to be plotted
    #
    x_list = []
    y_list = []

    # iterate solution
    #
    while t <= t_max:

        # record results
        #
        x_list.append(s.x)
        y_list.append(s.y)

        # calculate Runge Kutta coefficients for displacement and velocity
        #
        ks_1 = a(s)
        kv_1 = v

        ks_2 = a(s + kv_1 * dt/2)
        kv_2 = v + ks_1 * dt/2

        ks_3 = a(s + kv_2 * dt/2)
        kv_3 = v + ks_2 * dt/2

        ks_4 = a(s + kv_3 * dt)
        kv_4 = v + ks_3 * dt

        # predict new displacement and velocity
        #
        t += dt
        v = v + (dt/6) * (ks_1 + 2 * ks_2 + 2 * ks_3 + ks_4)
        s = s + (dt/6) * (kv_1 + 2 * kv_2 + 2 * kv_3 + kv_4)
    
    # display results
    #
    fig, ax = plt.subplots(1, 1)
    ax.set_title('Earth orbit (365 days)')
    ax.plot(x_list, y_list, label='position')
    ax.set_aspect('equal', 'box')
    ax.grid()
    plt.show()

if __name__== '__main__':
    main()