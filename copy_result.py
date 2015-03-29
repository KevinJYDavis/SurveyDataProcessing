# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:38:36 2015

@author: Kevin JY Davis
"""
#Script 6
"""Script that copies each processed feature class of survey data into the
processed geodatabase and then appends the survey records from each file into the
master tree geodatabase."""

import arcpy, os, datetime

def main():

    def mod_date(filename):
        """get modification date of a file"""
        return datetime.date.fromtimestamp(os.path.getmtime(filename))
    arcpy.env.workspace = r"E:\Data Collection\UnProcessedSurvey"
    surveyDict = {}

    rawKmz = arcpy.ListFiles('*.KM*')
    for kmz in rawKmz:
        kmzPath = os.path.join(arcpy.env.workspace,kmz)
        kmzBase = os.path.splitext(kmz)[0]
        surveyDate = mod_date(kmzPath).strftime('%m%d%Y')
        surveyDict[kmzBase] = surveyDate
        
    arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
    copyLoc = r"E:\Data Collection\Trees\Processed.gdb\SecondCycle" #processed geodatabase
    out = r"E:\Data Collection\Trees\SecondCycle.gdb\Master" #master geodatabase
    keep = [i for i in arcpy.ListFeatureClasses() if i[-3:] != '_AA']
    ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
    for x in ftc:
        ftcPath = os.path.join(arcpy.env.workspace,x)
        dropFields = ['Join_Count', 'TARGET_FID']
        arcpy.DeleteField_management(ftcPath, dropFields)
        outBase = x[:-3]
        outName = outBase + '_' + surveyDict[outBase]
        outData = os.path.join(copyLoc, outName)
        arcpy.Copy_management(ftcPath,outData)
        arcpy.Append_management(ftcPath, out, "TEST", "")
    return
if __name__ == '__main__':
  main()
