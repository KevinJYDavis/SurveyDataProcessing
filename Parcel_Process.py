import arcpy
arcpy.env.workspace = r"E:\Data Collection\Parcel\Parcel.gdb"
ftc = [f for f in arcpy.ListFeatureClasses()]
finalFields = ["OBJECTID", "SHAPE_Area", "SHAPE_Length", "SHAPE","LOC_ID","SITE_ADDR", "ADDR_NUM", "FULL_STR", "CITY"]
for x in ftc:
    fieldNames = [f.name for f in arcpy.ListFields(x)]
    dropFields = [z for z in fieldNames if z not in finalFields]
    arcpy.DeleteField_management(x, dropFields)
    

