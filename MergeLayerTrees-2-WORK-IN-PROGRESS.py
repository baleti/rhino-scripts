import rhinoscriptsyntax as rs
import scriptcontext as sc

a=rs.GetLayer("Get First Layer to Merge")
b=rs.GetLayer("Get Second Layer to Merge")

c = rs.LayerNames()

sc.doc.Objects.FindByLayer

a