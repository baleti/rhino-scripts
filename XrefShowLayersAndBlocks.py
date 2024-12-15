import rhinoscriptsyntax as rs
import scriptcontext as sc

def GetXrefLayers():
    a=rs.LayerNames()
    b=[i.replace('xref-AR000::', '') for i in a if "xref-AR000::" in i]
    c=rs.MultiListBox(b)
    return c

def XrefShowLayersAndBlocks():
    layers = GetXrefLayers()
    for layer in layers:
        objects = sc.doc.Objects.FindByLayer(layer)
        rs.LayerVisible(layer, visible=True)
        rs.ShowObjects(objects)

XrefShowLayersAndBlocks()