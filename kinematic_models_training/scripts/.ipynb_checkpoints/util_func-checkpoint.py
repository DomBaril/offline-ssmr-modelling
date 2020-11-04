#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def powerTrain_vel(tau_c, tau_d, cmd_vel, model_vel, index, dt):

    if cmd_vel[index] > -13 and cmd_vel[index] < 13:
        cmd_delay_index = int(index - tau_d / dt)
        new_vel = model_vel[index] + (1 / tau_c) * (cmd_vel[cmd_delay_index] - model_vel[index]) * dt
    
    elif cmd_vel[index] <= -13:
        new_vel = -13
        
    else:
        new_vel = 13

    return new_vel

def central_diff(f_over, f_under, d):
    
    return (f_over - f_under) / (2 * d)


def quaternion_to_euler(w, x, y, z):
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x**2 + y**2)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.where(np.abs(sinp) >= 1,
                     np.sign(sinp) * np.pi / 2,
                     np.arcsin(sinp))

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y**2 + z**2)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw

def comp_disp(x_fut, x_pres):
    x_disp = x_fut - x_pres
    return np.linalg.norm(x_disp)

def disp_err(x_pred, x):
    x_err = x_pred - x
    return x_err @ x_err

def wrap2pi(angle):
    if angle <= np.pi and angle >= -np.pi:
        return(angle)
    elif angle < -np.pi:
        return(wrap2pi(angle + 2*np.pi))
    else:
        return(wrap2pi(angle - 2*np.pi))
    
def up_propa_mat(mat, ang):
    propa_cos = np.cos(ang)
    propa_sin = np.sin(ang)
    mat[0,0] = propa_cos
    mat[0,1] = -propa_sin
    mat[1,0] = propa_sin
    mat[1,1] = propa_cos
    
    return mat