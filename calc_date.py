# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:29:25 2015

@author: Kevin
"""
#Script 5
"""Script that calculates the survey date of trees based on the last modification
date of the kml file that the trees are located in"""
import arcpy, os, datetime

def main():

  def mod_date(filename):
    """Get the modification date of a file"""
    return datetime.date.fromtimestamp(os.path.getmtime(filename))
  arcpy.env.workspace = r"E:\Data Collection\UnProcessedSurvey"
  surveyDict = {}

  #Get modification date for each KMZ file and associate the base file name with a date
  rawKmz = arcpy.ListFiles('*.KM*')
  for kmz in rawKmz:
    kmzPath = os.path.join(arcpy.env.workspace,kmz)
    kmzBase = os.path.splitext(kmz)[0]
    surveyDate = mod_date(kmzPath)
    surveyDict[kmzBase] = surveyDate
  
  arcpy.env.workspace = r"E:\Data Collection\ProcessedSurvey\SurveyTrees.gdb"
  keep = [i for i in arcpy.ListFeatureClasses() if i[-3:] != '_AA']
  ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
  for x in ftc:
    base = x[:-3]
    getSurveyDate = surveyDict[base] #Find the survey date associated with the base file name
    arcpy.CalculateField_management(x, "Survey_Date","'"  + str(getSurveyDate) + "'", "PYTHON_9.3", "#")
  return
if __name__ == '__main__':
  main()
