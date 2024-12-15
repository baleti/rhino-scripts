import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def GetNames():
    object_names = [object.Name for object in sc.doc.Objects if object.Name]
    format = "\n".join(sorted(set(object_names)))
    Rhino.UI.Dialogs.ShowTextDialog(format, "Block Names")

GetNames()