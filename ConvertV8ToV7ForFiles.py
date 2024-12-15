import os
import rhinoscriptsyntax as rs
import System
import subprocess


dlg = System.Windows.Forms.OpenFileDialog()
dlg.Multiselect = True
if dlg.ShowDialog()==System.Windows.Forms.DialogResult.OK:
    selected_files = dlg.FileNames

for i, selected_file in enumerate(selected_files):
    with open(os.environ['TEMP'] + "\\converting-madness-" + str(i) + ".cmd", "w") as madness:
        
        selected_file_path, selected_file_name = os.path.split(selected_file)
        if not os.path.exists(selected_file_path + "\\v7"):
            os.mkdir(selected_file_path + "\\v7")
        
        madness.write('start /min "" "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" /nosplash /runscript="-saveas version=7 ' + '""' + selected_file_path + "\\v7\\" + selected_file_name + '""' + ' exit" ' + chr(34) + selected_file + chr(34))
        madness.flush()
        subprocess.Popen(madness.name, shell=True)