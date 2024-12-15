import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc


def RemapView():
    
    vp = sc.doc.Views.ActiveView.ActiveViewport
    
    plane1 = vp.ConstructionPlane()
    
    rc, view = Rhino.Input.RhinoGet.GetView("Select the view with the target CPlane")
    
    if view.ActiveViewport.Name == vp.Name:
        return
        
    x = view.ActiveViewport
    if rc!=Rhino.Commands.Result.Success:
        return
    
    plane2 = view.ActiveViewport.ConstructionPlane()

    xform = Rhino.Geometry.Transform.PlaneToPlane(plane1, plane2)
    info = Rhino.DocObjects.ViewportInfo(vp)
    
    info.TransformCamera(xform)
    
    vp.SetCameraLocation(info.CameraLocation, False)
    vp.SetCameraTarget(info.TargetPoint, False)
    vp.SetCameraDirection (info.CameraDirection, True)
    vp.CameraUp = (info.CameraUp)
    sc.doc.Views.Redraw()

if __name__ == '__main__':
    RemapView()