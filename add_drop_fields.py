# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:58:11 2015

@author: Kevin JY Davis
"""
#Script 2
"""Script that organizes the fields for each survey tree feature class"""

import arcpy, os, datetime

def main():

  arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
  keep = ['UnitBoundaries_112913','WORTaxPar', 'Template']
  ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
  for x in ftc:
    arcpy.AddField_management(x, "Species", "TEXT", "", "", "255", "Species", "", "", "")
    arcpy.AddField_management(x, "DBH", "SHORT", "", "", "", "DBH", "", "", "")
    arcpy.AddField_management(x, "Survey_Date", "DATE", "", "", "", "Survey_Date", "","","")
    arcpy.CalculateField_management(x,"DBH","[PopupInfo]","VB","#")
    arcpy.CalculateField_management(x,"Species","str( !Name!)","PYTHON_9.3","#")
    fieldNames = [f.name for f in arcpy.ListFields(x)]
    finalFields = ['OBJECTID','Shape', 'Species', 'DBH', 'Survey_Date']
    dropFields = [z for z in fieldNames if z not in finalFields]
    arcpy.DeleteField_management(x, dropFields)
  return
if __name__ == '__main__':
  main()
