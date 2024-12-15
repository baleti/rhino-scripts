import rhinoscriptsyntax as rs
import subprocess
import os

if rs.GetDocumentUserText("Child") is None:
    dwg_folder_path = rs.BrowseForFolder("Choose folder to save DWGs into")
    files = rs.OpenFileNames("Choose files to save as DWG")
    for file in files: 
        subprocess.Popen('start "" /min "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" ' + \
                        '/nosplash /runscript="-SetDocumentUserText Child Child ' + \
                        '-SetDocumentUserText Export_DWG_folder_path ' + \
                        chr(34) + chr(34) + dwg_folder_path + chr(34) + chr(34) + ' ' + \
                        '-RunPythonScript (' + __file__ + ') -Exit No" ' + \
                        chr(34) + file + chr(34), shell=True)
else:
    dwg_folder_path_child = rs.GetDocumentUserText("Export_DWG_folder_path")
    rs.Command("-SaveAs " + chr(34) + dwg_folder_path_child + "\\" + \
                os.path.splitext(rs.DocumentName())[0] + ".dwg" + chr(34))
    rs.Command("-Exit No")