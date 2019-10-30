# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:00:44 2019

@author: Gareth Lomax
"""

import datashader as ds
import pandas as pd
from colorcet import fire
from datashader import transfer_functions as tf


df = pd.read_csv('./data/ged191.csv' )#, usecols=['dropoff_x', 'dropoff_y'])
df.head()

agg = ds.Canvas().points(df, 'longitude', 'latitude')
tf.set_background(tf.shade(agg, cmap=fire),"black")
#ds.utils.export_image(agg, "test_im")