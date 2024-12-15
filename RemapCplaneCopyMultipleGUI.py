import rhinoscriptsyntax as rs

named_cplanes = rs.NamedCPlanes()
selected_cplanes_from = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map from")
selected_cplanes_to = rs.MultiListBox(sorted(named_cplanes), "Cplane to Map to")

current_cplane = rs.ViewCPlane()

rs.RestoreNamedCPlane(selected_cplanes_from)

for selected_cplane_to in selected_cplanes_to:
    rs.Command("RemapCplane Copy=Yes Cplane " + chr(34) + selected_cplane_to + chr(34))

#restore previous Cplane
rs.ViewCPlane(plane=current_cplane)