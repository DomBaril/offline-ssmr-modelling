#!/usr/bin/env python

import numpy as np

def diff_drive(u, k):
    # u : [Vl, Vr], k : [r, B]
    J = k[0] *  np.array([[0.5, 0.5], [0.0, 0.0], [-1 / k[1], 1 / k[1]]])
    
    x = J @ u

    return x

def icr_diff_drive(u, k):
    # u : [Vl, Vr], k : [alpha_l, alpha_r, x_icr, y_icr_l, y_icr_r]
    
#     body_velocity_x = ((-y_icr_r * alpha_l * Vl) + (y_icr_l * alpha_r * Vr)) / (y_icr_l - y_icr_r)
#     body_velocity_y = ((x_icr * alpha_l * Vl) + (-x_icr * alpha_r * Vr))/ (y_icr_l - y_icr_r)
#     body_velocity_phi = ((-alpha_l * Vl) + (alpha_r) * Vr) / (y_icr_l - y_icr_r)
    
    J = 0.3 / (k[3] - k[4]) * (np.array([[-k[4], k[3]], [k[2], -k[2]], [-1, 1]]) @  np.array([[k[0], 0.0], [0.0, k[1]]]))
    
    x_dot = J @ u

    return x_dot

def extd_diff_drive_asym(Vl, Vr, x_icr, y_icr_l, y_icr_r, alpha_l, alpha_r):
    body_velocity_x = ((-y_icr_r * alpha_l * Vl) + (y_icr_l * alpha_r * Vr)) / (y_icr_l - y_icr_r)
    body_velocity_y = ((x_icr * alpha_l * Vl) + (-x_icr * alpha_r * Vr))/ (y_icr_l - y_icr_r)
    body_velocity_phi = ((-alpha_l * Vl) + (alpha_r) * Vr) / (y_icr_l - y_icr_r)

    return body_velocity_x, body_velocity_y, body_velocity_phi