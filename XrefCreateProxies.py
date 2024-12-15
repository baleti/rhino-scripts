import rhinoscriptsyntax as rs
import subprocess
import os

if rs.GetDocumentUserText("Child") is None:
    files = rs.OpenFileNames("choose files to create proxies")
    for file in files: 
        subprocess.Popen('start "" /min "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" /nosplash /runscript="-SetDocumentUserText Child Child -RunPythonScript (G:\\0000 CAD LIBRARY\\Scripts\\rhino\\CreateProxies.py) -Exit No" ' + chr(34) + file + chr(34), shell=True)
else:
    rs.Command("SelSmall 4000")
    rs.Command("SelBlockInstance")
    rs.Command("Delete")
    rs.Command("-Purge _Enter")
    rs.Command("-SaveAs " + chr(34) + rs.DocumentPath() + "\\proxy\\" + os.path.splitext(rs.DocumentName())[0] + "-proxy" + chr(34))
    rs.Command("Exit")