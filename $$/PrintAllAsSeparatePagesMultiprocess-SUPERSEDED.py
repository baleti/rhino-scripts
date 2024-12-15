import os
import subprocess
import rhinoscriptsyntax as rs

with open(os.environ['TEMP'] + "\\printing-madness" + ".cmd", "w") as madness:
    madness.write('start /min "" "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" /nosplash /runscript="-RunPythonScript (G:\\0000 CAD LIBRARY\\Scripts\\rhino\\_PrintAllAsSeparatePages.py) -Exit No" ' + chr(34) + rs.DocumentPath() + "\\" + rs.DocumentName() + chr(34))
    madness.flush()
    subprocess.Popen(madness.name, shell=True)