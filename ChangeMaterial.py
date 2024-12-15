import rhinoscriptsyntax as rs
import scriptcontext as sc

def ChangeMaterial():
    material_names = [i.Name for i in sc.doc.RenderMaterials]
    selected_material_name = rs.ComboListBox(sorted(material_names))
    
    if selected_material_name == None:
        return
    
    for material in sc.doc.RenderMaterials:
        if material.Name == selected_material_name:
            selected_material = material
    
    selected_objects = rs.GetObjects(preselect=True)
    
    if selected_objects == None:
        return
    
    for selected_object_guid in selected_objects:
        selected_object = rs.coercerhinoobject(selected_object_guid)
        selected_object.RenderMaterial = selected_material
        selected_object.CommitChanges()

ChangeMaterial()