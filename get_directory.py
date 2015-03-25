import Tkinter as tk
import tkFileDialog, os, datetime, glob, arcpy

def mod_date(filename):
    """Function for finding the date of last modification of a particular file"""
    return datetime.date.fromtimestamp(os.path.getmtime(filename))

def get_info():
    root = tk.Tk()
    root.withdraw()
    dirPath = tkFileDialog.askdirectory() #get file path
    return dirPath

x = get_info()
print x
##    g = dirPath + '/*.kmz'
##    for files in glob.glob(g):
##        toFeature(files)
##    return
##
##def toFeature(f):
##    fileName = os.path.basename(f) #get file name
##    fileBase = os.path.splitext(fileName)[0] #get file name with no extension
##    surveyDate = mod_date(f).strftime('%m%d%Y')
##    newFileBase = fileBase + "_" + surveyDate
##    print newFileBase
    
    
    
