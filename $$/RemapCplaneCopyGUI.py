import rhinoscriptsyntax as rs
import scriptcontext as sc

#doesn't work when this section turned on - try using transforms instead:

#selected_obj = rs.coercerhinoobject(rs.GetObject(preselect=True))
#if str(selected_obj.ObjectType) == "InstanceReference":
#    selected_obj_name = selected_obj.InstanceDefinition.Name
#else:
#    selected_obj_name = ""

named_cplanes = [i.Name for i in list(sc.doc.NamedConstructionPlanes.GetEnumerator())]
selected_cplane_from = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map from")
selected_cplane_to = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map to")


#doesn't work when this section turned on - try using transforms instead:
#message_from = "Name: " + selected_obj_name + "\n" + "Cplane to Map from"
#message_to = "Name: " + selected_obj_name + "\n" + "Cplane to Map to"

#selected_cplane_from = rs.ComboListBox(sorted(named_cplanes), message=message_from)
#selected_cplane_to = rs.ComboListBox(sorted(named_cplanes), message=message_to)


current_cplane = rs.ViewCPlane()
rs.RestoreNamedCPlane(selected_cplane_from)

rs.Command("RemapCplane Copy=Yes Cplane " + chr(34) + selected_cplane_to + chr(34))

#restore previous Cplane
rs.ViewCPlane(plane=current_cplane)