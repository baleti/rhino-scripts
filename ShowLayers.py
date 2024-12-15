import rhinoscriptsyntax as rs

def ShowLayers():
    layers=rs.GetLayers()
    for layer in layers:
        rs.LayerVisible(layer, visible=True)

ShowLayers()