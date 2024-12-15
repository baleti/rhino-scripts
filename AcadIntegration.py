import rhinoscriptsyntax as rs
from datetime import datetime
import os

buffer_folder = rs.GetDocumentData("ACAD_Exports", "Folder")
if buffer_folder is None:
    buffer_folder = rs.BrowseForFolder()
    rs.SetDocumentData("ACAD_Exports", "Folder", buffer_folder)

file_name = buffer_folder + os.path.sep + \
datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3] + "-" + \
rs.DocumentName() + ".dwg"

rs.Command("-_Export " + chr(34) + file_name + chr(34))

