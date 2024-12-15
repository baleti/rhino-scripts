import rhinoscriptsyntax as rs

object_guids = rs.GetObjects(preselect=True)
if len(object_guids) > 1:
    object_layers = list(set([rs.ObjectLayer(i) for i in object_guids]))
    selected_layer = rs.ComboListBox(object_layers)
    rs.CurrentLayer(selected_layer)
else:
    rs.CurrentLayer(rs.ObjectLayer(object_guids[0]))