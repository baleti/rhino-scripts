import rhinoscriptsyntax as rs
import scriptcontext as sc
from Rhino.DocObjects import DetailViewObject

def SetObjectsName():
    selected_objects = rs.SelectedObjects()
    if selected_objects == None: return
    
    objects_viewports = {i.Name for i in sc.doc.Objects if type(i) == DetailViewObject}
    
    if len(selected_objects) == 1:
        message = rs.coercerhinoobject(selected_objects[0]).Name
    else:
        message="Set Objects (Viewports) Name"
    
    name = rs.ComboListBox(sorted(list(objects_viewports)), message=message, title="All Named Objects")
    if name == None: return
    
    rs.ObjectName(selected_objects, name)

SetObjectsName()