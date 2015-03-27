# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:47:32 2015

@author: Kevin JY Davis
"""

"""This series of scripts will process data using the following workflow outline:
1. Convert tree points from KML to feature class
2. Add spatial attributes and remove extraneous attributes
3. Tranform from WGS1984 to Massachusetts Mainland Stateplane FIPS meters"""

"""Script for batch processing KML files to GDB feature classes"""

import arcpy, os

def main():
  
  def featClass(x,y,z):
    arcpy.FeatureClassToFeatureClass_conversion(x,y,z)
    return

  def toKML(x,y):
    arcpy.KMLToLayer_conversion(x,y)
    return
  
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
  return
if __name__ == '__main__':
  main()