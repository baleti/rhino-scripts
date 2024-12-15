import rhinoscriptsyntax as rs
import scriptcontext  as sc
import Rhino

selected_materials = list()

# get materials of blocks' sub-objects
# looping through all objects due to: https://discourse.mcneel.com/t/let-selcolor-command-select-objects-inside-blocks/151883/12
for object in sc.doc.Objects:
    if type(object) == Rhino.DocObjects.InstanceObject:
        sub_object_ids = object.GetSelectedSubObjects()
        if sub_object_ids:
            for sub_object_id in sub_object_ids:
                sub_object = object.InstanceDefinition.GetObjects()[sub_object_id.Index]
                if sub_object.RenderMaterial:
                    sub_object_material = sub_object.RenderMaterial.Id
                    selected_materials.append(sub_object_material)

# get materials of other objects
for object_id in rs.SelectedObjects():
    object = rs.coercerhinoobject(object_id)
    if object.RenderMaterial:
        object_material = object.RenderMaterial.Id
        selected_materials.append(object_material)

def _SelMaterial(object):
    for sub_object_id, sub_object in enumerate(object.InstanceDefinition.GetObjects()):
        if type(sub_object) == Rhino.DocObjects.InstanceObject:
            _SelMaterial(sub_object)
        if sub_object.RenderMaterial and sub_object.RenderMaterial.Id in selected_materials:
            object.SelectSubObject(Rhino.Geometry.ComponentIndex(Rhino.Geometry.ComponentIndexType.InstanceDefinitionPart, sub_object_id), True, True, True)

# select objects by material recursively, even though doesn't work for nested blocks
# https://discourse.mcneel.com/t/let-selcolor-command-select-objects-inside-blocks/151883/13
for object in sc.doc.Objects:
    if type(object) == Rhino.DocObjects.InstanceObject:
        _SelMaterial(object)

rs.EnableRedraw()
rs.Redraw()
