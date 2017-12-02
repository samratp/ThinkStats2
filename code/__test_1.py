# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:49:57 2017

@author: Samrat
"""

import nsfg

df = nsfg.ReadFemPreg()

df.describe()
df.columns

pregorder = df['pregordr']
pregorder = df.pregordr