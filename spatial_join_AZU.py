# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:27:29 2015

@author: Kevin JY Davis
"""
#Script 3
"""Script that spatially joins each tree to the unit it is located in"""

import arcpy, os
def main():
    arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
    path = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
    keep = ['UnitBoundaries_112913','WORTaxPar', 'Template']
    azu = 'UnitBoundaries_112913'
    ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
    for x in ftc:
        ftcPath = os.path.join(arcpy.env.workspace,x)
        azuOut = x + "_A"
        joinOut = os.path.join(path, azuOut)
        arcpy.SpatialJoin_analysis(ftcPath,azu,joinOut,
                                   "JOIN_ONE_TO_ONE","KEEP_ALL",
                               """Species "Species" true true false 255 Text 0 0 ,First,"""
                               """#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/Template,Species,-1,-1;DBH "DBH" true"""
                               """true false 2 Short 0 0 ,First,#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/Template"""
                               """,DBH,-1,-1;Survey_Date "Survey_Date" true true false 8 Date 0 0 ,First,#,E:/Data"""
                               """Collection/ProcessedSurvey/SurveyTrees.gdb/Template,Survey_Date,-1,-1;ALB_Area"""
                               """ "ALB_Area" true true false 12 Text 0 0 ,First,#,E:/Data Collection/"""
                               """ProcessedSurvey/SurveyTrees.gdb/UnitBoundaries_112913,ALB_Area,-1,-1;ALB_Zone"""
                               """ "ALB_Zone" true true false 5 Text 0 0 ,First,#,E:/Data Collection/ProcessedSurvey/"""
                               """SurveyTrees.gdb/UnitBoundaries_112913,ALB_Zone,-1,-1;ALB_Unit "ALB_Unit" true true false"""
                               """ 5 Text 0 0 ,First,#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/UnitBoundaries_112913,"""
                               """ALB_Unit,-1,-1;A_Z_U "A_Z_U" true true false 20 Text 0 0 ,First,#,E:/Data """
                               """Collection/ProcessedSurvey/SurveyTrees.gdb/UnitBoundaries_112913,A_Z_U,-1,-"""
                               """1""","INTERSECT","#","#")
    return
if __name__ == '__main__':
  main()

    
