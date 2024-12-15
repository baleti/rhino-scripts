import rhinoscriptsyntax as rs
import os
import subprocess
import System

dlg = System.Windows.Forms.OpenFileDialog()
dlg.Multiselect = True
if dlg.ShowDialog()==System.Windows.Forms.DialogResult.OK:
    selected_files = dlg.FileNames

#for selected_file in selected_files:
#    subprocess.Popen(["C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe", "/nosplash",
#                        '/runscript="-RunPythonScript (G:\\0000 CAD LIBRARY\\Scripts\\rhino\\SetLayerPrintWidthsToMatchCTB.py) save exit"',
#                        selected_file], close_fds=True, shell=True)

for i, selected_file in enumerate(selected_files):
    with open(os.environ['TEMP'] + "\\madness" + str(i) + ".cmd", "w") as madness:
        madness.write('start /min "" "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" /nosplash /runscript="-RunPythonScript (G:\\0000 CAD LIBRARY\\Scripts\\rhino\\SetLayerPrintWidthsToMatchCTB.py) save exit" ' + chr(34) + selected_file + chr(34))
        madness.flush()
        subprocess.Popen(madness.name, shell=True)
