#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def powerTrain_vel(tau_c, tau_d, cmd_vel, model_vel, index, dt):

    if cmd_vel[index] > -13 and cmd_vel[index] < 13:
        if tau_d < 0.000001:
            cmd_delay_index = index
        else:
            cmd_delay_index = int(index - tau_d / dt)
        new_vel = model_vel[index] + (1 / tau_c) * (cmd_vel[cmd_delay_index] - model_vel[index]) * dt
    
    elif cmd_vel[index] <= -13:
        new_vel = -13
        
    else:
        new_vel = 13

    return new_vel

def central_diff(f_over, f_under, d):
    
    return (f_over - f_under) / (2 * d)

# Differential Drive function
def diff_drive(Vl, Vr, r, B):
    body_velocity_x = r * (Vl / 2 + Vr / 2)
    body_velocity_phi = r * (-Vl / B + Vr / B)

    return body_velocity_x, body_velocity_phi