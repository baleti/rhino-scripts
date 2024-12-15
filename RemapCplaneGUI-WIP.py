import rhinoscriptsyntax as rs
import scriptcontext as sc

named_cplanes = [i.Name for i in list(sc.doc.NamedConstructionPlanes.GetEnumerator())]
selected_cplane_to = rs.ComboListBox(named_cplanes, "Cplane to Map to")
selected_cplane_from = rs.ComboListBox(named_cplanes, "Cplane to Map from")

rs.ViewCPlane(plane=selected_cplane_to)
rs.Command("RemapCplane Cplane " + selected_cplane)