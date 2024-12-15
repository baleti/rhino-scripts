import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

vp = sc.doc.Views.ActiveView.ActiveViewport

named_cplanes = [i.Name for i in sc.doc.NamedConstructionPlanes]
selected_cplane_name_from = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map from")
selected_cplane_name_to = rs.ComboListBox(sorted(named_cplanes), "Cplane to Map to")

for i in sc.doc.NamedConstructionPlanes:
    if i.Name == selected_cplane_name_from:
        plane1 = i.Plane
    if i.Name == selected_cplane_name_to:
        plane2 = i.Plane

xform = Rhino.Geometry.Transform.PlaneToPlane(plane1, plane2)
info = Rhino.DocObjects.ViewportInfo(vp)

info.TransformCamera(xform)

vp.SetCameraLocation(info.CameraLocation, False)
vp.SetCameraTarget(info.TargetPoint, False)
vp.SetCameraDirection (info.CameraDirection, True)
vp.CameraUp = (info.CameraUp)
sc.doc.Views.Redraw()