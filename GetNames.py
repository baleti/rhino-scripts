import rhinoscriptsyntax as rs
import Rhino

def GetNames():
    selected_object_ids = rs.SelectedObjects()
    if selected_object_ids == None: return
    
    selected_object_names = [rs.coercerhinoobject(id).Name for id in selected_object_ids if rs.coercerhinoobject(id).Name]
    format = "\n".join(sorted(set(selected_object_names)))
    Rhino.UI.Dialogs.ShowTextDialog(format, "Object Names")

GetNames()