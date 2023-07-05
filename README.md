# Orbit
Simulates 2D orbital motion in an *n*-body system.

## Model
The bodies attract each other due to Newton's classical laws of gravity.

This creates patterns of motion governed by a system of second order ordinary differential equations.

The simulation estimates the positions of the bodies over time using a 4th order *Runge-Kutta* scheme.

## Implementation
The program is written in pure python with `matplotlib` to show the results.

Two custom classes are used in order to keep the *Runge-Kutta* calculations as straightforward as possible.

The classes extend the basic arithmetic operations to 2D vectors and numeric lists. This permits the RK4 calculations to be represented with simple algebra even though the operations themselves occur between lists of vectors.

The classes are:

* **Vec2**: a class representing a 2D vector supporting vector addition, magnitude, and scalar multiplication.
* **NumList**: a subclass of `list` that supports element-wise addition and multiplication. 

## Usage
The program simulates the motions of the bodies over the defined timescale and then plots the results on a 2D canvas.

The initial masses, positions and velocities of the bodies are configured in the `initialisation` section of the main loop.

The time step `dt` and duration `t_max` should be chosen according to the sensitivity of the system.

Due to the behavior of `matplotlib` it is necessary to close the plot window before re-running the simulation.