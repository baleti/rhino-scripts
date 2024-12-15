import Rhino
import scriptcontext
import rhinoscriptsyntax as rs

def SelectObjectLayer():
    
    obj_id = rs.GetObjects(preselect=True)
    if not obj_id: return
    
    rh_obj = rs.coercerhinoobject(obj_id, True, True)
    layer_index = rh_obj.Attributes.LayerIndex
    
    scriptcontext.doc.Layers.Select([layer_index], True)
    
SelectObjectLayer()