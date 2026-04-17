
import numpy as np
import scipy.integrate as integrate

def simulate_triple_pendulum(time, x0, params):
    g = params["g"]
    L = params["L"]
    m = params["m"]

    def dx(x, t):
        theta1, theta2, theta3, p1, p2, p3 = x

        c12 = np.cos(theta1-theta2)
        c13 = np.cos(theta1-theta3)
        c23 = np.cos(theta2-theta3)

        Delta = 112 - 81*c12**2 + 81*c12*c13*c23 - 36*c13**2 - 63*c23**2

        A = np.array([
            [48 - 27*c23**2, -54*c12 + 27*c13*c23, 81*c12*c23 - 72*c13],
            [-54*c12 + 27*c13*c23, 84 - 27*c13**2, 81*c12*c13 - 126*c23],
            [81*c12*c23 - 72*c13, 81*c12*c13 - 126*c23, 336 - 243*c12**2]
        ])

        dtheta = (1/(m*L**2)) * (A @ np.array([p1,p2,p3])) / Delta
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

        return np.array([dtheta1,dtheta2,dtheta3,dp1,dp2,dp3])

    return integrate.odeint(dx, x0, time)
