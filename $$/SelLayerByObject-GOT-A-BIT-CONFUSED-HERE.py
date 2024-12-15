import scriptcontext as sc
import rhinoscriptsyntax as rs

object_id = rs.GetObject(preselect=True)
object_layer = rs.ObjectLayer(object_id)
a=rs.ObjectsByLayer(object_layer)
a

#this won't work - rs.ObjectsByLayer doesn't accept lists
#if object_ids:
#    object_layers = []
#    for object_id in object_ids:
#        object_layers.append(rs.ObjectLayer(object_id))
#    
#    rs.ObjectsByLayer(object_layers)