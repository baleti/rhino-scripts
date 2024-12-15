import rhinoscriptsyntax as rs

layer_tree_from=rs.GetLayers(title="Select Parent Layer to Merge From")
layer_tree_to=rs.GetLayers(title="Select Parent Layer to Merge To")