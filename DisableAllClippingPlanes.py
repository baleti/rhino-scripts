import scriptcontext as sc
import Rhino

def DisableAllClippingPlanes():
    
    clipping_planes = [i for i in sc.doc.Objects if type(i) == Rhino.DocObjects.ClippingPlaneObject]
    
    for clipping_plane in clipping_planes:
        clipping_plane.RemoveClipViewport(sc.doc.Views.ActiveView.ActiveViewport, True)

DisableAllClippingPlanes()