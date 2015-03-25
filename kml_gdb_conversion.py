#Batch process KML to GDB
import Tkinter as tk
import arcpy, os, tkFileDialog

def get_info():
    root = tk.Tk()
    root.withdraw()
    dirPath = tkFileDialog.askdirectory() #get directory path
    return dirPath

arcpy.env.workspace = get_info()

outLocation = "I:\\ARC\\WIP\\KevinWIP\\Data Collection\\GoogleEarthPro\\Processed"
MasterGDB = 'SurveyTrees.gdb'
MasterGDBLoc = os.path.join(outLocation, MasterGDB)

arcpy.CreateFileGDB_management(outLocation, MasterGDB)

# Convert all KMZ and KML files found in the current workspace
for kmz in arcpy.ListFiles('*.KM*'):
  print "CONVERTING: " + os.path.join(arcpy.env.workspace,kmz)
  arcpy.KMLToLayer_conversion(kmz, outLocation)

arcpy.env.workspace = outLocation

wks = arcpy.ListWorkspaces('*', 'FileGDB')
wks.remove(MasterGDBLoc)


for fgdb in wks:
    arcpy.env.workspace = fgdb
    featureClasses = arcpy.ListFeatureClasses('*', '', 'Placemarks')
    for fc in featureClasses:
        print "COPYING: " + fc + " FROM: " + fgdb    
        fcCopy = fgdb + os.sep + 'Placemarks' + os.sep + fc    
        arcpy.FeatureClassToFeatureClass_conversion(fcCopy, MasterGDBLoc, fgdb[fgdb.rfind(os.sep)+1:-4])


