import arcpy, os
arcpy.env.workspace = r"E:\Data Collection\GoogleEarthPro\Processed\SurveyTrees.gdb"
path = r"E:\Data Collection\GoogleEarthPro\Processed\SurveyTrees.gdb"
keep = ['UnitBoundaries_112913','WORTaxPar']
ftc = [f for f in arcpy.ListFeatureClasses() if f not in keep]
for x in ftc:
    azuOut = x + "_A"
    joinOut = os.path.join(path, azuOut)
    arcpy.SpatialJoin_analysis(x,azu,joinOut,
                           "JOIN_ONE_TO_ONE","KEEP_ALL",
                           """Species "Species" true true false 255 Text 0 0 ,First,"""
                           """#,E:/Data Collection/GoogleEarthPro/Processed/SurveyTrees.gdb"""
                           """/WOR_7_102,Species,-1,-1;DBH "DBH" true true false 2 Short 0 0 ,"""
                           """First,#,E:/Data Collection/GoogleEarthPro/Processed/SurveyTrees.gdb"""
                           """/WOR_7_102,DBH,-1,-1;ALB_Area "ALB_Area" true true false 12 Text 0 0 ,"""
                           """First,#,E:/Data Collection/GoogleEarthPro/Processed/SurveyTrees.gdb"""
                           """/UnitBoundaries_112913,ALB_Area,-1,-1;ALB_Zone """
                           """"ALB_Zone" true true false 5 Text 0 0 ,First,#,E:/Data Collection"""
                           """/GoogleEarthPro/Processed/SurveyTrees.gdb/UnitBoundaries_112913,"""
                           """ALB_Zone,-1,-1;ALB_Unit "ALB_Unit" true true false 5 Text 0 0 ,"""
                           """First,#,E:/Data Collection/GoogleEarthPro/Processed/SurveyTrees.gdb"""
                           """/UnitBoundaries_112913,ALB_Unit,-1,-1;A_Z_U "A_Z_U" """
                           """true true false 20 Text 0 0 ,First,#,E:/Data Collection"""
                           """/GoogleEarthPro/Processed/SurveyTrees.gdb/UnitBoundaries_112913,"""
                           """A_Z_U,-1,-1""","INTERSECT","#","#")
    
