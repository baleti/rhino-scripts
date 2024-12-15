# need to find a way to escape the last command

import rhinoscriptsyntax as rs

named_cplanes = rs.NamedCPlanes()
new_name = rs.ComboListBox(sorted(named_cplanes))
rs.Command("-NamedCplane Delete " + chr(34) + new_name + chr(34) + " Enter")