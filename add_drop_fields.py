import arcpy
arcpy.env.workspace = r"E:\Data Collection\GoogleEarthPro\Processed\SurveyTrees.gdb"
keep = ['UnitBoundaries_112913','WORTaxPar']
ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
for x in ftc:
    arcpy.AddField_management(x, "Species", "TEXT", "", "", "255", "Species", "", "", "")
    arcpy.AddField_management(x, "DBH", "SHORT", "", "", "", "DBH", "", "", "")
    arcpy.CalculateField_management(x,"DBH","int( !PopupInfo!)","PYTHON_9.3","#")
    arcpy.CalculateField_management(x,"Species","str( !Name!)","PYTHON_9.3","#")
    fieldNames = [f.name for f in arcpy.ListFields(x)]
    finalFields = ['OBJECTID','Shape', 'Species', 'DBH']
    dropfields = [z for z in fieldNames if z not in finalFields]
    arcpy.DeleteField_management(x, dropfields)
