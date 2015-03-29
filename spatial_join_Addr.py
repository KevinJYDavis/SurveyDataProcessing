# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:39:43 2015

@author: Kevin JY Davis
"""
#Script 4
"""Script that spatially joins each tree to the parcel it is located in."""

import arcpy, os
def main():
    arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
    path = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
    addr = 'WORTaxPar' #We'll have to append all the parcels together for this
    keep = [i for i in arcpy.ListFeatureClasses() if i[-2:] != '_A']
    ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
    for x in ftc:
        ftcPath = os.path.join(arcpy.env.workspace,x)
        addrOut = x + "A"
        joinOut = os.path.join(path, addrOut)
        arcpy.SpatialJoin_analysis(ftcPath, addr, joinOut,
                                   "JOIN_ONE_TO_ONE", "KEEP_ALL",
                                   """Species "Species" true true false 255 Text 0 0 ,First,#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/"""
                                   """Template,Species,-1,-1;DBH "DBH" true true false 4 Long 0 0 ,First,#,E:/Data Collection/"""
                                   """ProcessedSurvey/SurveyTrees.gdb/Template,DBH,-1,-1;Survey_Date "Survey_Date" true true false 8 Date 0 0 ,First,"""
                                   """#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/Template,Survey_Date,-1,-1;ALB_Area """
                                   """"ALB_Area" true true false 12 Text 0 0 ,First,#,E:/Data Collection/ProcessedSurvey/"""
                                   """SurveyTrees.gdb/Template,ALB_Area,-1,-1;ALB_Zone "ALB_Zone" true true false 5 Text 0 0 ,First,#,E:/"""
                                   """Data Collection/ProcessedSurvey/SurveyTrees.gdb/Template,ALB_Zone,-1,-1;ALB_Unit "ALB_Unit" true true false 5 Text 0 0 ,First,"""
                                   """#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/Template,ALB_Unit,-1,-1;"""
                                   """A_Z_U "A_Z_U" true true false 20 Text 0 0 ,First,#,E:/Data Collection/ProcessedSurvey/SurveyTrees.gdb/"""
                                   """Template,A_Z_U,-1,-1;LOC_ID "LOC_ID" true false false 18 Text 0 0 ,First,#,E:/Data Collection/"""
                                   """ProcessedSurvey/SurveyTrees.gdb/WORTaxPar,LOC_ID,-1,-1;SITE_ADDR "SITE_ADDR" true true false 255 Text 0 0 ,First,#,E:/Data """
                                   """Collection/ProcessedSurvey/SurveyTrees.gdb/WORTaxPar,SITE_ADDR,-1,-1;ADDR_NUM "ADDR_NUM" true true false 255 Text 0 0 ,First,#,E:/Data """
                                   """Collection/ProcessedSurvey/SurveyTrees.gdb/WORTaxPar,ADDR_NUM,-1,-1;FULL_STR "FULL_STR" true true false 255 Text 0 0 ,First,#,E:/Data """
                                   """Collection/ProcessedSurvey/SurveyTrees.gdb/WORTaxPar,FULL_STR,-1,-1;CITY "CITY" true true false 255 Text 0 0 ,First,#,E:/Data """
                                   """Collection/ProcessedSurvey/SurveyTrees.gdb/WORTaxPar,CITY,-1,-1""","INTERSECT","#","#")
    return
if __name__ == '__main__':
  main()
                               
