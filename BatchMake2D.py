import Rhino.Geometry
from Rhino.DocObjects import ObjectType
from Rhino.Display import RhinoPageView
import scriptcontext as sc
import rhinoscriptsyntax as rs

def BatchMake2D():
    selected_page_names = rs.MultiListBox([i.PageName for i in sc.doc.Views.GetPageViews()])
    if selected_page_names == None:
        return
    selected_pages = [i for i in sc.doc.Views.GetPageViews() if i.PageName in selected_page_names]
    
    for selected_page in selected_pages:
        all_detail_views = RhinoPageView.GetDetailViews(selected_page)
        
        #select views by "CGeo" in the name
        #in the future autogenerate corresponding views based on geolocation (EarthAnchorPoint)
        target_views = [detail_view for detail_view in all_detail_views if detail_view.Name and "CGeo" in detail_view.Name]
        if len(target_views) == 0:
            rs.MessageBox("No '-CGeo' viewports found.\nAdd corresponding named viewports.\nBatch Make2D will exit now.")
            return
        
        for source_view in all_detail_views:
            if source_view.Name == None:
                continue
            if "CGeo" in source_view.Name:
                continue
            
            first_corner = Rhino.Geometry.Point2d(source_view.Viewport.Bounds.Left, source_view.Viewport.Bounds.Bottom)
            second_corner = Rhino.Geometry.Point2d(source_view.Viewport.Bounds.Right, source_view.Viewport.Bounds.Top)
            
            
            for vp in all_detail_views:
                if vp.Name and source_view.Name in vp.Name and "CGeo" in vp.Name:
                    target_viewport = vp.Viewport
                    break
                else:
                    target_viewport = None
            if target_viewport == None:
                continue
            
            source_view.IsActive = True
            
            sc.doc.Objects.UnselectAll()
            #https://discourse.mcneel.com/t/how-to-get-coordinates-of-a-viewport-corners/153493
            rhino_objects = sc.doc.Objects.FindByCrossingWindowRegion(source_view.Viewport, 
                                                                    first_corner, second_corner, 
                                                                    True, ObjectType.AnyObject)
            rs.SelectObjects(rhino_objects)
            
            #transform Make2D results to the correct location (based on chosen real-world "geolocation")
            source_viewport_plane = Rhino.Geometry.Plane(source_view.Viewport.CameraTarget, 
                                                source_view.Viewport.CameraX, 
                                                source_view.Viewport.CameraY)
            target_viewport_plane = Rhino.Geometry.Plane(target_viewport.CameraTarget, 
                                                target_viewport.CameraX, 
                                                target_viewport.CameraY)
            
            xform = Rhino.Geometry.Transform.PlaneToPlane(source_viewport_plane, target_viewport_plane)
            
            rs.Command("CPlane View _Enter")
            rs.Command("-Make2D Layout=CPlane Properties=MaintainSourceLayers CreateHiddenLines=No ShowTangents=No CreateSceneSilhouette=No CreateClippingPlaneIntersections=No ShowViewRectangle=No GroupOutput=No LayerName " + source_view.Name + " _Enter")
            rs.Command("_Enter")
            make2d_results = rs.SelectedObjects()
            rs.TransformObjects(make2d_results, xform, copy=False)
            
            sc.doc.Objects.UnselectAll()
            source_view.IsActive = False

BatchMake2D()