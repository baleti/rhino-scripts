import os
import rhinoscriptsyntax as rs
import scriptcontext as sc
import System
import subprocess
import Rhino

block_defs = list(sc.doc.InstanceDefinitions.GetList(ignoreDeleted=True))

for idx, block_def in enumerate(block_defs):
    if rs.IsBlockEmbedded(block_def.Name) == False and ".3dm" in block_def.SourceArchive:
        with open(os.environ['TEMP'] + "\\converting-madness-" + str(idx) + ".cmd", "w") as madness:
            
            xref_folder, xref_file_name = os.path.split(block_def.SourceArchive)
            if not os.path.exists(xref_folder + "\\RhinoV7"):
                os.mkdir(xref_folder + "\\RhinoV7")
            
            madness.write('start /min "" "C:\\Program Files\\Rhino 8 WIP\\System\\Rhino.exe" /nosplash /runscript="-RunPythonScript (G:\\0000 CAD LIBRARY\\Scripts\\rhino\\_XrefFilePathSourceV7.py) -saveas version=7 ' + '""' + xref_folder + "\\RhinoV7\\" + xref_file_name + '""' + ' -Exit No" ' + chr(34) + block_def.SourceArchive + chr(34))
            madness.flush()
            subprocess.Popen(madness.name, shell=True)

for idx, block_def in enumerate(block_defs):
    if rs.IsBlockEmbedded(block_def.Name) == False and ".3dm" in block_def.SourceArchive:
        block_folder, block_file_name = os.path.split(block_def.SourceArchive)
        new_block_path = block_folder + "\\RhinoV7\\" + block_file_name
        sc.doc.InstanceDefinitions.ModifySourceArchive(block_def.Index,
                            new_block_path,
                            Rhino.DocObjects.InstanceDefinitionUpdateType.Linked,
                            0)

document_name, document_ext = os.path.splitext(rs.DocumentName())
rs.Command("-saveas version=7 " + chr(34) + rs.DocumentPath() + document_name + "-V7" + document_ext + chr(34))
subprocess.Popen(rs.DocumentPath() + document_name + "-V7" + document_ext)
rs.Command("-Exit No")