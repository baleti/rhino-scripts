import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def SetClippingPlanesName():
    selected_objects = rs.SelectedObjects()
    if selected_objects == None: return
    
    objects = {i.Name for i in sc.doc.Objects if type(i) == Rhino.DocObjects.ClippingPlaneObject}
    
    if len(selected_objects) == 1:
        message = rs.coercerhinoobject(selected_objects[0]).Name
    else:
        message="Set Objects Name"
    
    name = rs.ComboListBox(list(objects), message=message, title="All Named Objects")
    if name == None: return
    
    rs.ObjectName(selected_objects, name)

SetClippingPlanesName()