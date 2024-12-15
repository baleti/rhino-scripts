import rhinoscriptsyntax as rs
import Rhino

def GetLayers():
    object_ids = rs.GetObjects(preselect=True)
    
    if object_ids:
        object_layers = set()
        for object_id in object_ids:
            object_layer = rs.ObjectLayer(object_id)
            object_layers.add(object_layer)
        format = "\n".join(sorted(object_layers))
        Rhino.UI.Dialogs.ShowTextDialog(format, "Block Names")
#        rs.ComboListBox(sorted(list(object_layers)))

GetLayers()