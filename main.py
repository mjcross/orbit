import matplotlib.pyplot as plt
from vec2 import Vec2

mu = 132712440042e9     # standard gravitational parameter of the sun (m3/s2)
r_perihelion = 147100e6 # orbit radius of earth at perihelion (m)
v_perihelion = 30.29e3  # average orbital velocity (m/s)

v0 = Vec2(v_perihelion, 0)     # initial velocity vector
y0 = Vec2(0, r_perihelion)     # initial position vector

h = 24 * 60 * 60        # 1 day
t_max = 365 * h         # 1 year (approx)

def a(r):
    """ acceleration at displacement r (vector) """
    k = mu / pow(abs(r), 3)
    a = Vec2( -k * r.x, -k * r.y)
    return a


def main():
    # initialisation
    #  
    t = 0
    v = v0
    y = y0

    t_list = []
    pos_x = []
    pos_y = []

    # iterate solution
    #
    while t <= t_max:

        # record results
        #
        pos_x.append(y.x)
        pos_y.append(y.y)

        # calculate p and q coefficients
        #
        p1 = a(y)
        q1 = v

        p2 = a(y + q1 * h/2)
        q2 = v + p1 * h/2

        p3 = a(y + q2 * h/2)
        q3 = v + p2 * h/2

        p4 = a(y + q3 * h)
        q4 = v + p3 * h

        # update parameters
        #
        t += h
        v = v + (h/6) * (p1 + 2 * p2 + 2 * p3 + p4)
        y = y + (h/6) * (q1 + 2 * q2 + 2 * q3 + q4)
    
    # display results
    #
    fig, ax = plt.subplots(1, 1)
    ax.set_title('Earth orbit (365 days)')
    ax.plot(pos_x, pos_y, label='position')
    ax.set_aspect('equal', 'box')
    ax.grid()
    plt.show()

if __name__== '__main__':
    main()