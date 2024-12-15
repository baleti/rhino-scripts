import rhinoscriptsyntax as rs
import scriptcontext as sc

named_cplanes = [i.Name for i in list(sc.doc.NamedConstructionPlanes.GetEnumerator())]
selected_cplanes_from = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map from")
selected_cplane_to = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map to")

current_cplane = rs.ViewCPlane()
rs.RestoreNamedCPlane(selected_cplanes_from)

rs.Command("RemapCplane Copy=Yes Cplane " + chr(34) + selected_cplane_to + chr(34))

#restore previous Cplane
rs.ViewCPlane(plane=current_cplane)