# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:38:18 2015

@author: apkdavis
"""
#Script 7
"""Script that cleans up after processing ALB survey data"""

import arcpy, os
def main():
    
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
        ftcPath = os.path.join(arcpy.env.workspace,x)
        arcpy.Delete_management(ftcPath)
    return
if __name__ == '__main__':
    main()
