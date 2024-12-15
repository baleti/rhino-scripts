import rhinoscriptsyntax as rs
import scriptcontext as sc

def HideLayers():
    layers=rs.GetLayers()
    for layer in layers:
        rs.LayerVisible(layer, visible=False)

# couldn't figure out a faster way to do this :(
def HideLayers2():
    selected_layer = rs.GetLayer()
    layer_object = sc.doc.Layers.Find()
    layer_object.IsVisible = False

HideLayers()