import rhinoscriptsyntax as rs
import scriptcontext as sc

layer_names = rs.LayerNames()
xref_layers = [i.replace('xref-AR000::', '') for i in layer_names if "xref-AR000::" in i]
selected_layers = rs.MultiListBox(xref_layers)

for layer_short_name in selected_layers:
    layer_index = sc.doc.Layers.FindByFullPath('xref-AR000::' + layer_short_name,
                                                notFoundReturnValue=False)
    layer_object = sc.doc.Layers.FindIndex(layer_index)
    # ^= XOR toggling value on and off
    layer_object.IsVisible ^= True