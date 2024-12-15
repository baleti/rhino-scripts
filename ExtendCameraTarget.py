import rhinoscriptsyntax as rs
import scriptcontext as sc

def PushTarget():
    
    vp = sc.doc.Views.ActiveView.ActiveViewport
    t = vp.CameraTarget
    c = vp.CameraLocation
    
    factor = 1.25
    if sc.sticky.has_key('TARGET_FACTOR'):
        factor = sc.sticky['TARGET_FACTOR']
    
    factor = rs.GetReal('Factor', factor, minimum= .1, maximum = None)
    if not factor: return
    
    sc.sticky['TARGET_FACTOR']= factor
    
    vecDir = t-c
    vecDir = vecDir * factor
    
    vp.SetCameraTarget (c+ vecDir, False)
    
    sc.doc.Views.Redraw()
    
if __name__ == '__main__':PushTarget()