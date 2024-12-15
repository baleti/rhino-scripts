import rhinoscriptsyntax as rs
import subprocess
import os

if rs.GetDocumentUserText("Child") is None:
    files = rs.OpenFileNames("choose files to convert curves to lines")
    for file in files: 
        subprocess.Popen('start "" /min "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" ' + \
                        '/nosplash /runscript="-SetDocumentUserText Child Child ' + \
                        '-RunPythonScript (' + __file__ + ')" ' + \
                        chr(34) + file + chr(34), shell=True)
else:
    rs.Command("_SelLine")
    rs.Command("_Convert Output=Lines SimplifyInput=No DeleteInput=Yes OutputLayer=Input _Enter")
    rs.Command("Save")
    rs.Command("Exit")