"""Export folder is same as current folder if file has been saved;
otherwise, choice of location.
Change format on line 18.
Script by Mitch Heynick 08.07.19"""

import rhinoscriptsyntax as rs
import scriptcontext as sc
import os

def ExportObjectsToSeparateFiles():
    names = rs.GetObjects(preselect=True)
    
    #get folder to save file in
    folder=rs.WorkingFolder()
    doc_path=rs.DocumentPath()
    ft="3dm"
    msg="Main file name/folder for {} export?".format(ft)
    if doc_path:
        msg+=" (Enter to save in current folder)".format(ft)
        folder=doc_path
    save_folder = rs.BrowseForFolder(folder,msg)
    if not save_folder: return
    
    #start the export sequence
    rs.EnableRedraw(False)
    for name in names:
        e_file_name = '{}.{}'.format(name,ft.lower())
        filename=os.path.join(save_folder,str(e_file_name))
        rs.UnselectAllObjects()
        rs.SelectObject(name, redraw=False)
        #runs the export using the file name/path and your settings
        rs.Command('-_Export "{}" _Enter'.format(filename), echo=True)
    rs.UnselectAllObjects()
    rs.EnableRedraw(True)

ExportObjectsToSeparateFiles()
