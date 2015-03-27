# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:38:18 2015

@author: apkdavis
"""
#Script 7
"""Script that cleans up after processing tree data"""

import arcpy, os
scratch = []

arcpy.env.workspace = r'E:\Data Collection\ProcessedSurvey'
workDir = r'E:\Data Collection\ProcessedSurvey'
saveGDB = r'E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb'
files = arcpy.ListFiles('*')

for x in files:
    scratch.append(os.path.join(workDir, x))
scratch.remove(saveGDB)
for y in scratch:
    arcpy.Delete_management(y)

arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
keep = ['UnitBoundaries_112913','WORTaxPar', 'Template']
ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
for x in ftc:
    arcpy.Delete_management(x)
