import rhinoscriptsyntax as rs

layers = rs.GetLayers(title="Select Layers to move")
layer_parent = rs.GetLayer(title="Select Parent")

for layer in layers:
    rs.ParentLayer(layer, layer_parent)
