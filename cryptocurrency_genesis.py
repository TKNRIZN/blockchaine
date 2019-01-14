#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:19:08 2019

@author: takanori
"""

from cryptocurrency_block import *
import datetime as date



def create_genesis_block():
    return Block(0,date.datetime.now(),"Genesis Block","0")