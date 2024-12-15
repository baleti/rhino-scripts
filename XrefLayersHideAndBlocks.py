import rhinoscriptsyntax as rs
import scriptcontext as sc

def GetXrefLayers():
    a=rs.LayerNames()
    b=[i.replace('xref-AR000::', '') for i in a if "xref-AR000::" in i]
    c=rs.MultiListBox(b)
    return c

def XrefLayersHideAndBlocks():
    layers = GetXrefLayers()
    for layer in layers:
        objects = sc.doc.Objects.FindByLayer(layer)
        rs.HideObjects(objects)
        rs.LayerVisible(layer, visible=False)

XrefLayersHideAndBlocks()