import matplotlib.pyplot as plt
from vec2 import Vec2

mu = 132712440042e9     # standard gravitational parameter of the sun (m3/s2)
r_perihelion = 147100e6 # orbit radius of earth at perihelion (m)
v_perihelion = 30.29e3  # average orbital velocity (m/s)

v0 = Vec2(v_perihelion, 0)     # initial velocity vector
s0 = Vec2(0, r_perihelion)     # initial position vector

dt = 24 * 60 * 60       # 1 day
t_max = 365 * dt         # 1 year (approx)

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

    # list of coordinates to be plotted
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

        # calculate p and q coefficients
        #
        p1 = a(s)
        q1 = v

        p2 = a(s + q1 * dt/2)
        q2 = v + p1 * dt/2

        p3 = a(s + q2 * dt/2)
        q3 = v + p2 * dt/2

        p4 = a(s + q3 * dt)
        q4 = v + p3 * dt

        # update parameters
        #
        t += dt
        v = v + (dt/6) * (p1 + 2 * p2 + 2 * p3 + p4)
        s = s + (dt/6) * (q1 + 2 * q2 + 2 * q3 + q4)
    
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