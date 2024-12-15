import rhinoscriptsyntax as rs
import scriptcontext as sc

def ChangeCameraProjection():
    projection_type = ["Parallel", "Perspective", "Two Point"]
    projection_selected = rs.ComboListBox(projection_type)
    
    if projection_selected == None:
        return
    
    if projection_selected == "Parallel":
        sc.doc.Views.ActiveView.ActiveViewport.ChangeToParallelProjection(symmetricFrustum=True)
        rs.EnableRedraw(True)
        rs.Redraw()
    if projection_selected == "Perspective":
        sc.doc.Views.ActiveView.ActiveViewport.ChangeToPerspectiveProjection(symmetricFrustum=False, lensLength=60)
        rs.EnableRedraw(True)
        rs.Redraw()
    if projection_selected == "Two Point":
        sc.doc.Views.ActiveView.ActiveViewport.ChangeToTwoPointPerspectiveProjection(lensLength=60)
        rs.EnableRedraw(True)
        rs.Redraw()

ChangeCameraProjection()