import scriptcontext as sc
import rhinoscriptsyntax as rs

object_ids = rs.GetObjects(preselect=True)

if object_ids:
    object_layers = []
    for object_id in object_ids:
        object_layers.append(rs.ObjectLayer(object_id))
    
    rs.ObjectsByLayer(object_layers)