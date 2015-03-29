# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:47:32 2015

@author: Kevin JY Davis
"""

"""This series of scripts will process data using the following workflow outline:
1. Convert tree points from KML to feature class
2. Add spatial attributes and remove extraneous attributes
3. Clean up intermediate workspaces, retaining the original kmz files,
The output feature classes, feature classes for spatial joining and the
master tree feature class"""

#Script 1
"""Script for batch processing KML files to GDB feature class"""

import arcpy, os

def main():
  
  def featClass(x,y,z):
    arcpy.FeatureClassToFeatureClass_conversion(x,y,z)
    return

  def toKML(x,y):
    arcpy.KMLToLayer_conversion(x,y)
    return

  arcpy.env.overwriteOutput = True
  arcpy.env.workspace = r"E:\Data Collection\UnProcessedSurvey"
  outLocation = r"E:\Data Collection\ProcessedSurvey"
  MasterGDB = "SurveyTrees.gdb"
  MasterGDBLoc = os.path.join(outLocation, MasterGDB)
  #arcpy.CreateFileGDB_management(outLocation, MasterGDB)

  # Convert all KMZ and KML files found in the current workspace
  rawKmz = arcpy.ListFiles('*.KM*')
  for kmz in rawKmz:
    toKML(kmz, outLocation)
    
  arcpy.env.workspace = outLocation

  wks = arcpy.ListWorkspaces('*')
  wks.remove(MasterGDBLoc)


  for fgdb in wks:
    arcpy.env.workspace = fgdb
    featureClasses = arcpy.ListFeatureClasses('*', '', 'Placemarks')
    for fc in featureClasses:   
      fcCopy = fgdb + os.sep + 'Placemarks' + os.sep + fc    
      featClass(fcCopy, MasterGDBLoc, fgdb[fgdb.rfind(os.sep)+1:-4])
  del wks, fgdb, fc
  return
if __name__ == '__main__':
  main()
