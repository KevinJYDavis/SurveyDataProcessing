# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:12:24 2015

@author: apkdavis
"""

##Data Processing Script for ALB survey data
"""This program will process data using the following workflow outline:
1. Convert tree points from KML to feature class
2. Add spatial attributes and remove extraneous attributes
3. Tranform from WGS1984 to Massachusetts Mainland Stateplane FIPS meters"""

"""Keys to making the program user friendly:
The only input will be the kml file. 
All other files will be created deleted altered and stored within the script. 
The output will have a user-friendly title and be easy to locate."""
import Tkinter as tk
import tkFileDialog, os
def toFeature():
    root = tk.Tk()
    root.withdraw()
    filePath = tkFileDialog.askopenfilename() #get file path
    fileName = os.path.basename(filePath) #get file name
    fileBase = os.path.splitext(fileName)[0] #get file name with no extension