# need to find a way to escape the last command

import rhinoscriptsyntax as rs

named_cplanes = rs.NamedCPlanes()
if not named_cplanes:
    named_cplanes = [" "]
new_name = rs.ComboListBox(sorted(named_cplanes), message="Name for the new Named Cplane")
rs.Command("-NamedCplane Save " + chr(34) + new_name + chr(34) + " Enter")