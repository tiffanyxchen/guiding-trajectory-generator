
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Freely Moving Pendulums in Vacuum

g : gravitational acceleration (planetary gravity)
L : lengths of the pendulums
m : masses of the pendulums

Simulates the positions of freely moving pendulums in vacuum 
using the Lagrangian formalism, starting from a given initial 
potential energy.

run: %matplotlib qt

Created on Tue Oct 7 12:59:47 2025

@author: Tiffany
"""
from src.utilities.save_states import save_state
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation # 
# from save_results import save_simulation_results
import time

from numba import jit

g = 9.8 # acceleration due to gravity, in m/s^2
L = 1.0 # length of pendulums
m = 1.0 # mass of pendulums

# @jit(nopython=True)
def dx(x,t):
    """
    The right-hand side of the pendulum ODE
    x=[x1,x2,x3,x4]
    """
    theta1, theta2, theta3, p1, p2, p3 = x
    
    # cosines
    c12 = np.cos(theta1 - theta2)
    c13 = np.cos(theta1 - theta3)
    c23 = np.cos(theta2 - theta3)
    
    # matrix M
    '''
    M = np.array([
        [7/3, 3/2*c12, 1/2*c13],
        [3/2*c12, 4/3, 1/2*c23],
        [1/2*c13, 1/2*c23, 1/3]
    ])
    '''
    
    # Inverse of M
    # Using symbolic formula from before
    Delta = 112 - 81*c12**2 + 81*c12*c13*c23 - 36*c13**2 - 63*c23**2
    A = np.array([
        [48 - 27*c23**2, -54*c12 + 27*c13*c23, 81*c12*c23 - 72*c13],
        [-54*c12 + 27*c13*c23, 84 - 27*c13**2, 81*c12*c13 - 126*c23],
        [81*c12*c23 - 72*c13, 81*c12*c13 - 126*c23, 336 - 243*c12**2]
    ])
    
    # Velocities: dtheta_i/dt = (1/(m*L^2)) * M^-1 @ p
    dtheta = (1/(m*L**2)) * (A @ np.array([p1, p2, p3])) / Delta
    
    dtheta1, dtheta2, dtheta3 = dtheta
    
    # dp_i/dt = ∂L/∂θ_i
    dp1 = -1.5*m*L**2*dtheta1*dtheta2*np.sin(theta1-theta2) \
          -0.5*m*L**2*dtheta1*dtheta3*np.sin(theta1-theta3) \
          -2.5*m*g*L*np.sin(theta1)
    
    dp2 = +1.5*m*L**2*dtheta1*dtheta2*np.sin(theta1-theta2) \
          -0.5*m*L**2*dtheta2*dtheta3*np.sin(theta2-theta3) \
          -1.5*m*g*L*np.sin(theta2)
    
    dp3 = +0.5*m*L**2*dtheta1*dtheta3*np.sin(theta1-theta3) \
          +0.5*m*L**2*dtheta2*dtheta3*np.sin(theta2-theta3) \
          -0.5*m*g*L*np.sin(theta3)
    
    return np.array([dtheta1, dtheta2, dtheta3, dp1, dp2, dp3])


# create a time array from 0..100 sampled at 0.1 second steps

# independent variable time
# -----------------------------
# ✅ TIME CONTROL (NEW)
# -----------------------------
t0 = 0.0
tf = 10.0
dt = 0.01

t = np.arange(t0, tf, dt)
#t = linspace(0,10.,800)
#dt = t[1]-t[0]
# initial state
x0 = array([-3.0416, -3.0416, -3.0416, 0.0, 0.0, 0.0])
theta_init = [-3.0416, -3.0416, -3.0416]

start_time = time.time()
# ----------------------
# Integrate
# ----------------------
# integrate your ODE using scipy.integrate.

x = integrate.odeint(dx, x0, t)

# -----------------------------
# ✅ SAVE STATE (NEW)
# -----------------------------
save_state(
    t,
    x,
    theta_init,
    tag="PY_ODE"
)




end_time = time.time()

print(f"ODE integration took {end_time - start_time:.4f} seconds")


x1 =   L * sin(x[:,0])
y1 = - L * cos(x[:,0])
x2 = x1 + L*sin(x[:,1])
y2 = y1 - L*cos(x[:,1])
x3 = x2 + L * sin(x[:, 2])
y3 = y2 - L * cos(x[:, 2])


fig, (ax_static, ax_anim) = plt.subplots(1, 2, figsize=(10, 5))

# ----------------------
# Static plot (t = 0)
# ----------------------
ax_static.set_xlim(-3*L, 3*L)
ax_static.set_ylim(-3*L, 3*L)
ax_static.grid()
ax_static.set_title(f"t = 0, theta_0 = {x0[0]:.2f}, {x0[1]:.2f}, {x0[2]:.2f}")

thisx0 = [0, x1[0], x2[0], x3[0]]
thisy0 = [0, y1[0], y2[0], y3[0]]

ax_static.plot(thisx0, thisy0, 'o-', lw=2)
ax_static.scatter(thisx0, thisy0, s=50)

# ----------------------
# Animation plot
# ----------------------
ax_anim.set_xlim(-3*L, 3*L)
ax_anim.set_ylim(-3*L, 3*L)
ax_anim.grid()
ax_anim.set_title("Evolution")

line, = ax_anim.plot([], [], 'o-', lw=2)
time_text = ax_anim.text(0.05, 0.9, '', transform=ax_anim.transAxes)

time_template = 'time = %.1fs'

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i], x3[i]]
    thisy = [0, y1[i], y2[i], y3[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i * dt))
    return line, time_text

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(t),
    interval=20,
    init_func=init,
    blit=False   # important for Spyder
)

plt.show()

# save_simulation_results(t, x, x1, y1, x2, y2, x3, y3, x0[0], x0[1], x0[2])
