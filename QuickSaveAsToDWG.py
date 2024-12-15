import rhinoscriptsyntax as rs
from datetime import datetime
import os

stash = rs.GetDocumentData("ACAD_SaveAs", "Folder")
if stash is None:
    stash = rs.BrowseForFolder(message="choose location to stash temporary exports - required only once per Rhino Document")
    rs.SetDocumentData("ACAD_SaveAs", "Folder", stash)

document_name = "Untitled"
if rs.DocumentName():
    document_name = rs.DocumentName()

file_name = stash + os.path.sep + \
datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3] + "-" + \
document_name + ".dwg"

rs.Command("-_SaveAs " + chr(34) + file_name + chr(34))

