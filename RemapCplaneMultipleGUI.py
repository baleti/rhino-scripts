# something's not workign - check remapcplanecopygui

import rhinoscriptsyntax as rs

def RemapCplaneCopyMultipleGUI():
    # if it's a block show it's name in the message title
    # should be developed to take other objects' names
    selected_obj = rs.coercerhinoobject(rs.GetObject(preselect=True))
    if str(selected_obj.ObjectType) == "InstanceReference":
        selected_obj_name = selected_obj.InstanceDefinition.Name
    else:
        selected_obj_name = ""
    
    named_cplanes = rs.NamedCPlanes()
    
    selected_cplane_from = rs.ComboListBox(sorted(named_cplanes), "Name: " + selected_obj_name + "\n" + "Cplane to Map from")
    selected_cplane_to = rs.ComboListBox(sorted(named_cplanes), "Name: " + selected_obj_name + "\n" + "Cplane to Map to")
    
    current_cplane = rs.ViewCPlane()
    rs.RestoreNamedCPlane(selected_cplane_from)
    
    if selected_cplane_from == None or selected_cplane_to == None:
        return
    
    # needs to find a way to take a list from a combolistbox
#    for selected_cplane_to in list(selected_cplanes_to):
    rs.Command("RemapCplane Copy=Yes Cplane " + chr(34) + selected_cplane_to + chr(34))
    
    #restore previous Cplane
    rs.ViewCPlane(plane=current_cplane)

RemapCplaneCopyMultipleGUI()