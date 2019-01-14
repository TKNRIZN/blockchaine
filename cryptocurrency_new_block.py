#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:21:36 2019

@author: takanori
"""

import datetime as date
from cryptocurrency_block import *

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! Im block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index,this_timestamp,this_data,this_hash)