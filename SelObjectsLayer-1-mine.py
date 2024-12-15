import scriptcontext as sc
import rhinoscriptsyntax as rs

ids = rs.SelectedObjects()

layers = [rs.ObjectLayer(id) for id in ids]
layers = list(set(layers))

for layer in layers:
    parent = rs.ParentLayer(layer)
    while parent is not None:
        rs.ExpandLayer(parent, True)
        parent = rs.ParentLayer(parent)

layers = [sc.doc.Layers.FindByFullPath(layer, -1) for layer in layers]
sc.doc.Layers.Select(layers, True)
