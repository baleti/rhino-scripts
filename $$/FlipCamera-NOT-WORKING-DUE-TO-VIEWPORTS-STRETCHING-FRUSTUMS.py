
import scriptcontext as sc

vp = sc.doc.Views.ActiveView.ActiveViewport
p1 = vp.CameraLocation
p2 = vp.CameraTarget
vecDir = p2-p1
p1 =  p1 + (vecDir*2)
vecDir.Reverse()

vp.SetCameraLocations(p2, p1)
sc.doc.Views.Redraw()

    