# Copyright (c) 2023, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

"""
Object for data and calculation
"""

from math import atan, degrees

EARTH_GRAVITATIONAL_ACCELERATION = 9.80665

class BVObject():
    def __init__(self, _m, _gf):
        self.mass = _m
        self.gforce_profile = _gf


