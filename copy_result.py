# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:38:36 2015

@author: Kevin JY Davis
"""
#Script 6
"""Script that copies each processed feature class of survey data into the
processed geodatabase and then appends the survey records from each file into the
master tree geodatabase."""

import arcpy, os

arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
copyLoc = r"E:\Data Collection\Trees\Processed.gdb\SecondCycle" #processed geodatabase
out = r"E:\Data Collection\Trees\SecondCycle.gdb\Master" #master geodatabase
keep = [i for i in arcpy.ListFeatureClasses() if i[-3:] != '_AA']
ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
for x in ftc:
    dropFields = ['Join_Count', 'TARGET_FID']
    arcpy.DeleteField_management(x, dropFields)
    outName = x[:-3]
    outData = os.path.join(copyLoc, outName)
    arcpy.Copy_management(x,outData)
    arcpy.Append_management(x, out, "TEST", "")
