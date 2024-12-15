# needs a FROM Cplane - could use NamedCplaneGUI.py

import rhinoscriptsyntax as rs
import scriptcontext as sc

#world_top_cplane = rs.PlaneFromPoints("0,0,0", "1,0,0", "0,1,0")

named_cplanes = [i.Name for i in list(sc.doc.NamedConstructionPlanes.GetEnumerator())]
selected_cplane_to = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map to")

#rs.coerceplane()

#rs.ViewCPlane(plane=world_top_cplane)
rs.Command("RemapCplane Cplane " + chr(34) + selected_cplane_to + chr(34))
#rs.Command("Cplane Undo Enter")