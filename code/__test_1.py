# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:49:57 2017

@author: Samrat
"""

import nsfg

df = nsfg.ReadFemPreg()

df.describe()
df.columns

#column access
pregorder = df['pregordr']
pregorder = df.pregordr
#indexing
pregorder[0]
#slicing
pregorder[0:10]

df['outcome'].value_counts().sort_index()
df.birthwgt_lb.value_counts(sort=False)
