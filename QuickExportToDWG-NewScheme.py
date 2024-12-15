import rhinoscriptsyntax as rs

current_cplane = rs.ViewCPlane()
rs.Command("Cplane World Top")
rs.Command('Export')
rs.ViewCPlane(plane=current_cplane)