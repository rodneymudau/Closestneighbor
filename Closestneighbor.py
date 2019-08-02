# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:44:07 2019

@author: Khumbelo

Given the names and GPS positions of 750 people
(latitude, longitude and elevation) find the 10
closest  neighbors of a randomly selected individual
"""

import numpy as np
from sklearn.neighbors import DistanceMetric

R = 6371 # approximate radius of earth in km

# coordinates in (lat,lon,elv) in units of (rad,rad,km)
coords = np.random.random((750, 3)) * 2
cart_coords = np.array([((R+coord[2]) * np.cos(coord[0]) * np.cos(coord[1]),
                         (R+coord[2]) * np.cos(coord[0]) * np.sin(coord[1]),
                         (R+coord[2]) *np.sin(coord[0])) for coord in coords])

# calculate distances between points
dist = DistanceMetric.get_metric('euclidean')
dist_vals = dist.pairwise(cart_coords)

# pick a random person
random_person = np.random.choice(np.arange(750))
top_ten = np.where(dist_vals[random_person] < sorted(dist_vals[random_person])[11])[0]
# remove self from list
top_ten = top_ten[top_ten!=random_person]

print(top_ten)


	
