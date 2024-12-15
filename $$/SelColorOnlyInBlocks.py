import rhinoscriptsyntax as rs
import scriptcontext  as sc
import Rhino

selected_colors = list()

# get colors of blocks' sub-objects
# looping through all objects due to: https://discourse.mcneel.com/t/let-selcolor-command-select-objects-inside-blocks/151883/12
for object in sc.doc.Objects:
    if type(object) == Rhino.DocObjects.InstanceObject:
        sub_object_ids = object.GetSelectedSubObjects()
        if sub_object_ids:
            for sub_object_id in sub_object_ids:
                sub_object = object.InstanceDefinition.GetObjects()[sub_object_id.Index]
                sub_object_color = sub_object.Attributes.DrawColor(sc.doc)
                selected_colors.append(sub_object_color)

# get colors of other objects
for object_id in rs.SelectedObjects():
    object = rs.coercerhinoobject(object_id)
    object_color = object.Attributes.DrawColor(sc.doc)
    selected_colors.append(object_color)

def _SelColor(object):
    for sub_object_id, sub_object in enumerate(object.InstanceDefinition.GetObjects()):
        if type(sub_object) == Rhino.DocObjects.InstanceObject:
            _SelColor(sub_object)
        if sub_object.Attributes.DrawColor(sc.doc) in selected_colors:
            object.SelectSubObject(Rhino.Geometry.ComponentIndex(Rhino.Geometry.ComponentIndexType.InstanceDefinitionPart, sub_object_id), True, True, True)

# select objects by color recursively, even though doesn't work for nested blocks
# https://discourse.mcneel.com/t/let-selcolor-command-select-objects-inside-blocks/151883/13
for object in sc.doc.Objects:
    if type(object) == Rhino.DocObjects.InstanceObject:
        _SelColor(object)

rs.EnableRedraw()
rs.Redraw()
