#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:49:14 2019

@author: hvyd
"""
import math
import matrix

def kalman_filter(x, P):
    for n in range(len(measurements)):
        
        # measurement update
        Z = matrix([[measurements[n]]])
        y = Z-(H*x)
        S = H*P*H.transpose() +R
        K = P* H.transpose()*S.inverse()
        x = x+(K*y)
        P = (I-(K*H))*P
        # prediction
        x = (F*x)+u
        P = F*P*F.transpose()
    return x,P



measurements = [1, 2, 3]

x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix([[1., 0.]]) # measurement function
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x, P))
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]
