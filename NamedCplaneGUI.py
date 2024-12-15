import rhinoscriptsyntax as rs
import scriptcontext as sc

named_cplanes = rs.NamedCPlanes()
if not named_cplanes:
    raise Exception("No Named CPlanes")
else:
    selected_cplane = rs.ComboListBox(sorted(named_cplanes), "Named CPlanes")

rs.RestoreNamedCPlane(selected_cplane)