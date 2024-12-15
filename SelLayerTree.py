import rhinoscriptsyntax as rs
import Rhino
"""Script written by Mitch Heynick version 02.07.15
Selects objects on chosen layers plus all nested sublayers
GetLayers() method is not yet implemented for Mac Rhino -
so choice is limited to a single layer with GetLayer() for the moment"""
def OnMac():
    return Rhino.Runtime.HostUtils.RunningOnOSX

def SelObjsLayerAndSubs(layer):
    rs.ObjectsByLayer(layer, True)
    subLayers = rs.LayerChildren(layer)
    if(subLayers):
        #layer has one or more sublayers
        for sLayer in subLayers:
            #recurse
            SelObjsLayerAndSubs(sLayer)

def SelLayerTree():
    if OnMac():
        layer=rs.GetLayer("Select layer for objects")
        if not layer: return
        layers=[layer]
    else:
        layers = rs.GetLayers("Select layers for objects")	
        if not(layers): return
    rs.EnableRedraw(False)
    rs.UnselectAllObjects()
    for pLayer in layers:
        SelObjsLayerAndSubs(pLayer)

SelLayerTree()