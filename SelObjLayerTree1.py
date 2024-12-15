import rhinoscriptsyntax as rs
import Rhino
"""
Gets selected objects' layers,then selects all objects on those layers plus all
other layers in the layer tree recursively - i.e. selects objects on layers both
"up" and "down" the tree.  Script by Mitch Heynick 17.12.18"""

def GetTopLevelLayer(layer):
    parent=rs.ParentLayer(layer)
    return parent

def SelObjsLayerAndSubs(layer):
    rs.ObjectsByLayer(layer, True)
    subLayers = rs.LayerChildren(layer)
    if(subLayers):
        #layer has one or more sublayers
        for sLayer in subLayers:
            #recurse
            SelObjsLayerAndSubs(sLayer)

def SelEntireObjLayerTree():
    objs=rs.GetObjects("Select objects",preselect=True,select=True)
    if not objs: return
    layers=set()
    for obj in objs:
        layers.add(GetTopLevelLayer(rs.ObjectLayer(obj)))
    rs.EnableRedraw(False)
    for layer in layers:
        SelObjsLayerAndSubs(layer)

SelEntireObjLayerTree()