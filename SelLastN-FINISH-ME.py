import rhinoscriptsyntax as rs
import scriptcontext as sc


aa=rs.LastObject()
#a=rs.GetObject(preselect=True)
b=rs.coercerhinoobject(aa)

c=sc.doc.Objects.AllObjectsSince(b.RuntimeSerialNumber)

print(type(c))

#[i.Select(True) for i in c[:2]]
