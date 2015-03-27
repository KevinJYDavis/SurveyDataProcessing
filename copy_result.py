# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:38:36 2015

@author: Kevin
"""

import arcpy, os

arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
out = r"E:\Data Collection\ProcessedSurvey\Processed.gdb"
keep = [i for i in arcpy.ListFeatureClasses() if i[-3:] != '_AA']
ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
for x in ftc:
    out_data = os.path.join(out, x)
    arcpy.Copy_management(x, out_data, "")
