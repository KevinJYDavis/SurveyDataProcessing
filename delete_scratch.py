#Rename fields in Survey Trees gdb

import arcpy, os
scratch = []

arcpy.env.workspace = 'I:\\ARC\\WIP\\KevinWIP\\Data Collection\\GoogleEarthPro\\Processed'
workDir = 'I:\\ARC\\WIP\\KevinWIP\\Data Collection\\GoogleEarthPro\\Processed'
saveGDB = 'I:\\ARC\\WIP\\KevinWIP\\Data Collection\\GoogleEarthPro\\Processed\\SurveyTrees.gdb'
files = arcpy.ListFiles('*')

for x in files:
    scratch.append(os.path.join(workDir, x))
scratch.remove(saveGDB)
print "Deleting: " + y
for y in scratch:
    arcpy.Delete_management(y)
