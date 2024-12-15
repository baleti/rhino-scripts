import rhinoscriptsyntax as rs
# add globbing
#import glob

named_layer_filters_str = rs.GetDocumentUserText("Named-Layer-Filters")

if named_layer_filters_str is None:
    selected_filter = rs.ComboListBox(["None"], message="Create a Named Layer Filter")
    rs.SetDocumentUserText("Named-Layer-Filters", selected_filter)
else:
    named_layer_filters_list = named_layer_filters_str.split(",")
    selected_filter = rs.ComboListBox(named_layer_filters_list)
    named_layer_filters_list.append(selected_filter)
    named_layer_filters_list_new = list(set(named_layer_filters_list))
    named_layer_filters_list_new_str = ",".join(named_layer_filters_list_new)
    rs.SetDocumentUserText("Named-Layer-Filters", named_layer_filters_list_new_str)

visible = rs.ComboListBox(["Show", "Hide"])
if visible == "Show":
    [rs.LayerVisible(layer, visible=True) for layer in rs.LayerNames() if selected_filter in layer]
if visible == "Hide":
    [rs.LayerVisible(layer, visible=False) for layer in rs.LayerNames() if selected_filter in layer]