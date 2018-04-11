# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:39:55 2018

@author: k1475052
"""

import pandas as pd
import win32ui
import win32con
o=win32ui.CreateFileDialog(1)
if o.DoModal()==1:
    filename=o.GetPathName()
#%% Import CSV file
    df=pd.read_csv(filename,',',header=0,
                   names=['ID','NAME','EMAIL','STATUS','ROUTE','MODULE_CODE','MODULE_NAME'])
    df['Student_Number']=df.SCJ_Code.str.split('/',expand=True)[0] #split and then return column 0 (firts column)
    #df=df[['','']]