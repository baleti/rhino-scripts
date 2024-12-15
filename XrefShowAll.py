#check if rewriting in RhinoCommon would be faster
#seems now that toggling layers' visibility is much faster

import rhinoscriptsyntax as rs

def XrefShowAll():
    all_layers = rs.LayerNames()
    xref_layers = [layer.replace('xref-AR000::', '') for layer in all_layers 
                    if "xref-AR000::" in layer]
    for xref_layer in xref_layers:
        rs.LayerVisible(xref_layer, visible=True)

XrefShowAll()